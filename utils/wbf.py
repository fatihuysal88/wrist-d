# coding: utf-8
import numpy as np
import pandas as pd
import json
import time
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from multiprocessing import Pool, Process, cpu_count, Manager
from ensemble_boxes import *
import os
from itertools import permutations
from itertools import combinations
import csv


class wbf:
    def __init__(self,gt_path="/content/drive/MyDrive/Makale_2/ground_truth/ground_truth.json"):
        self.gt_path = gt_path
        self.params =  {
            'run_type': 'wbf',
            'skip_box_thr': 0.3,
            'intersection_thr': 0.5,
            'conf_type': 'avg',
            'limit_boxes': 6000,
            'verbose': True,
        }

        

    def get_coco_annotations_data(self):
        file_in = self.gt_path
        images = dict()
        with open(file_in) as json_file:
            data = json.load(json_file)
            for i in range(len(data['images'])):
                image_id = data['images'][i]['id']
                images[image_id] = data['images'][i]

        return images

    def get_coco_score(self,csv_path):
        images = self.get_coco_annotations_data()
        s = pd.read_csv(csv_path, dtype={'img_id': np.str_, 'label': np.str_})
        out = np.zeros((len(s), 7), dtype=np.float64)
        out[:, 0] = s['img_id']
        ids = s['img_id'].astype(np.int32).values
        x1 = s['x1'].values
        x2 = s['x2'].values
        y1 = s['y1'].values
        y2 = s['y2'].values

        for i in range(len(s)):

            width = images[ids[i]]['width']
            height = images[ids[i]]['height']
            out[i, 1] = x1[i] * width
            out[i, 2] = y1[i] * height
            out[i, 3] = (x2[i] - x1[i]) * width
            out[i, 4] = (y2[i] - y1[i]) * height

        out[:, 5] = s['score'].values
        out[:, 6] = s['label'].values
        filename = 'new_test.json'
        coco_gt = COCO(self.gt_path)

        detections = out

        image_ids = list(set(detections[:, 0]))
        coco_dt = coco_gt.loadRes(detections)

        #**********************************
        annType = ['segm', 'bbox', 'keypoints']
        annType = annType[1]
        print_lrp_components_over_size = True
        #coco_eval = COCOeval(coco_gt, coco_dt, annType, print_lrp_components_over_size)
        #**********************************
        coco_eval = COCOeval(coco_gt, coco_dt, iouType='bbox')
        coco_eval.params.imgIds = image_ids
        coco_eval.evaluate()
        coco_eval.accumulate()
        coco_eval.summarize()
        coco_metrics = coco_eval.stats
        ap = coco_metrics[1]

        return ap

    def process_single_id(self, id, res_boxes, weights, params):
        run_type = params['run_type']
        verbose = params['verbose']

        # print('Go for ID: {}'.format(id))
        boxes_list = []
        scores_list = []
        labels_list = []
        labels_to_use_forward = dict()
        labels_to_use_backward = dict()

        for i in range(len(res_boxes[id])):
            boxes = []
            scores = []
            labels = []

            dt = res_boxes[id][i]

            for j in range(0, len(dt)):
                lbl = dt[j][5]
                scr = float(dt[j][4])
                box_x1 = float(dt[j][0])
                box_y1 = float(dt[j][1])
                box_x2 = float(dt[j][2])
                box_y2 = float(dt[j][3])

                if box_x1 >= box_x2:
                    if verbose:
                        print('Problem with box x1 and x2: {}. Skip it'.format(dt[j]))
                    continue
                if box_y1 >= box_y2:
                    if verbose:
                        print('Problem with box y1 and y2: {}. Skip it'.format(dt[j]))
                    continue
                if scr <= 0:
                    if verbose:
                        print('Problem with box score: {}. Skip it'.format(dt[j]))
                    continue

                boxes.append([box_x1, box_y1, box_x2, box_y2])
                scores.append(scr)
                if lbl not in labels_to_use_forward:
                    cur_point = len(labels_to_use_forward)
                    labels_to_use_forward[lbl] = cur_point
                    labels_to_use_backward[cur_point] = lbl
                labels.append(labels_to_use_forward[lbl])

            boxes = np.array(boxes, dtype=np.float32)
            scores = np.array(scores, dtype=np.float32)
            labels = np.array(labels, dtype=np.int32)

            boxes_list.append(boxes)
            scores_list.append(scores)
            labels_list.append(labels)

        # Empty predictions for all models
        if len(boxes_list) == 0:
            return np.array([]), np.array([]), np.array([])

        if run_type == 'wbf':
            merged_boxes, merged_scores, merged_labels = weighted_boxes_fusion(boxes_list, scores_list, labels_list,
                                                                               weights=weights,
                                                                               iou_thr=params['intersection_thr'],
                                                                               skip_box_thr=params['skip_box_thr'],
                                                                               conf_type=params['conf_type'])
        elif run_type == 'nms':
            iou_thr = params['iou_thr']
            merged_boxes, merged_scores, merged_labels = nms(boxes_list, scores_list, labels_list, weights=weights,
                                                             iou_thr=iou_thr)
        elif run_type == 'soft-nms':
            iou_thr = params['iou_thr']
            sigma = params['sigma']
            thresh = params['thresh']
            merged_boxes, merged_scores, merged_labels = soft_nms(boxes_list, scores_list, labels_list,
                                                                  weights=weights, iou_thr=iou_thr, sigma=sigma,
                                                                  thresh=thresh)
        elif run_type == 'nmw':
            merged_boxes, merged_scores, merged_labels = non_maximum_weighted(boxes_list, scores_list, labels_list,
                                                                              weights=weights,
                                                                              iou_thr=params['intersection_thr'],
                                                                              skip_box_thr=params['skip_box_thr'])

        # print(len(boxes_list), len(merged_boxes))
        if 'limit_boxes' in params:
            limit_boxes = params['limit_boxes']
            if len(merged_boxes) > limit_boxes:
                merged_boxes = merged_boxes[:limit_boxes]
                merged_scores = merged_scores[:limit_boxes]
                merged_labels = merged_labels[:limit_boxes]

        # Rename labels back
        merged_labels_string = []
        for m in merged_labels:
            merged_labels_string.append(labels_to_use_backward[m])
        merged_labels = np.array(merged_labels_string, dtype=np.str)

        # Create IDs array
        ids_list = [id] * len(merged_labels)

        return merged_boxes.copy(), merged_scores.copy(), merged_labels.copy(), ids_list.copy()

    def process_part_of_data(self, proc_number, return_dict, ids_to_use, res_boxes, weights, params):
        #print('Start process: {} IDs to proc: {}'.format(proc_number, len(ids_to_use)))
        result = []
        for id in ids_to_use:
            merged_boxes, merged_scores, merged_labels, ids_list = self.process_single_id(id, res_boxes, weights, params)
            # print(merged_boxes.shape, merged_scores.shape, merged_labels.shape, len(ids_list))
            result.append((merged_boxes, merged_scores, merged_labels, ids_list))
        return_dict[proc_number] = result.copy()

    def ensemble_predictions(self, pred_filenames, weights, params):
        verbose = False
        if 'verbose' in params:
            verbose = params['verbose']

        start_time = time.time()
        procs_to_use = max(cpu_count() // 2, 1)
        # procs_to_use = 6
        #print('Use processes: {}'.format(procs_to_use))
        weights = np.array(weights)

        res_boxes = dict()
        ref_ids = None
        for j in range(len(pred_filenames)):
            if weights[j] == 0:
                continue
            #print('Read {}...'.format(pred_filenames[j]))
            s = pd.read_csv(pred_filenames[j], dtype={'img_id': np.str_, 'label': np.str_})
            s.sort_values('img_id', inplace=True)
            s.reset_index(drop=True, inplace=True)
            ids = s['img_id'].values
            unique_ids = sorted(s['img_id'].unique())
            if ref_ids is None:
                ref_ids = tuple(unique_ids)
            else:
                if ref_ids != tuple(unique_ids):
                    #print('Different IDs in ensembled CSVs! {} != {}'.format(len(ref_ids), len(unique_ids)))
                    s = s[s['img_id'].isin(ref_ids)]
                    s.sort_values('img_id', inplace=True)
                    s.reset_index(drop=True, inplace=True)
                    ids = s['img_id'].values
            preds = s[['x1', 'y1', 'x2', 'y2', 'score', 'label']].values
            single_res = dict()
            for i in range(len(ids)):
                id = ids[i]
                if id not in single_res:
                    single_res[id] = []
                single_res[id].append(preds[i])
            for el in single_res:
                if el not in res_boxes:
                    res_boxes[el] = []
                res_boxes[el].append(single_res[el])

        # Reduce weights if needed
        weights = weights[weights != 0]

        ids_to_use = sorted(list(res_boxes.keys()))
        manager = Manager()
        return_dict = manager.dict()
        jobs = []
        for i in range(procs_to_use):
            start = i * len(ids_to_use) // procs_to_use
            end = (i + 1) * len(ids_to_use) // procs_to_use
            if i == procs_to_use - 1:
                end = len(ids_to_use)
            p = Process(target=self.process_part_of_data,
                        args=(i, return_dict, ids_to_use[start:end], res_boxes, weights, params))
            jobs.append(p)
            p.start()

        for i in range(len(jobs)):
            jobs[i].join()

        results = []
        for i in range(len(jobs)):
            results += return_dict[i]

        # p = Pool(processes=procs_to_use)
        # results = p.starmap(process_single_id, zip(ids_to_use, repeat(weights), repeat(params)))

        all_ids = []
        all_boxes = []
        all_scores = []
        all_labels = []
        for boxes, scores, labels, ids_list in results:
            if boxes is None:
                continue
            all_boxes.append(boxes)
            all_scores.append(scores)
            all_labels.append(labels)
            all_ids.append(ids_list)

        all_ids = np.concatenate(all_ids)
        all_boxes = np.concatenate(all_boxes)
        all_scores = np.concatenate(all_scores)
        all_labels = np.concatenate(all_labels)
        #if verbose:
            #print(all_ids.shape, all_boxes.shape, all_scores.shape, all_labels.shape)

        res = pd.DataFrame(all_ids, columns=['img_id'])
        res['x1'] = all_boxes[:, 0]
        res['y1'] = all_boxes[:, 1]
        res['x2'] = all_boxes[:, 2]
        res['y2'] = all_boxes[:, 3]
        res['score'] = all_scores
        res['label'] = all_labels
        #print('Run time: {:.2f}'.format(time.time() - start_time))
        return res

    def ensemble(self, benchmark_csv, weights, ensemble_name):
        
        for bcsv in benchmark_csv:
            print('Go for {}'.format(bcsv))
            print(bcsv)
            self.get_coco_score(bcsv)
        
        print("************************","Result of",ensemble_name,"************************")
        print("WBF Subset",benchmark_csv)
        print("WBF Weights",weights)
        ensemble_preds = self.ensemble_predictions(benchmark_csv, weights, self.params)
        ensemble_preds.to_csv(ensemble_name+".csv", index=False)

        # print(benchmark_csv)
        self.get_coco_score((ensemble_name+".csv"))
        

    def predict(self, subset, weights, ensemble_name):

        self.ensemble(list(subset), weights, ensemble_name)
