import time
from tqdm.notebook import tqdm
import json
import copy
from os import path
import csv
import glob


class mmdetection2wbf:
    def __init__(self, gt_path="new_test.json", json_path=None,csv_path=None, init=True):
        self.gt_path = gt_path
        self.json_path = json_path
        self.csv_path = csv_path
        self.init = init

    # **************************************************************************
    def _Open_Json(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
            print("Count of object is", len(data))
            for i in range(0, len(data)):
                data[i]['image_id'] = data[i]['image_id'][15:-1]
            f.close()
            return data

    # **************************************************************************
    def _json_2_Csv(self, name_csv, data):
        # json files is converted to csv files for usage wbf method
        target_path=self.csv_path+"/"+name_csv
        with open(target_path, 'w', encoding='UTF8', newline='') as _f:
            header = ['img_id', 'x1', 'y1', 'x2', 'y2', 'score', 'label', ]
            writer = csv.writer(_f)
            writer.writerow(header)
            image_width, image_height = None, None
            for i in range(0, len(data)):

                real_data = data[i]['bbox']

                with open(self.gt_path, 'r') as gt_file:
                    new_test_data = json.load(gt_file)
                    for k in range(0, 54):
                        if int(new_test_data["images"][k]['id']) == int(data[i]['image_id']):
                            image_width, image_height = new_test_data["images"][k]['width'], new_test_data["images"][k][
                                'height']

                gt_file.close()
                xn1 = real_data[0] / image_width
                yn1 = real_data[1] / image_height
                xn2 = (real_data[0] + real_data[2]) / image_width
                yn2 = (real_data[1] + real_data[3]) / image_height

                image_id = data[i]['image_id'][:]
                csv_data = [int(image_id), xn1, yn1, xn2, yn2, data[i]['score'], data[i]['category_id'], ]
                writer.writerow(csv_data)

    # **************************************************************************
    def _Edit_Gt_Label(self):


            with open(self.gt_path, 'r') as _f:
                print("Labels are loaded!")
                data_original = json.load(_f)
                data_new = copy.deepcopy(data_original)
            _f.close()
            print("Count of images is", len(data_original["images"]))
            print("Count of annotations is", len(data_original["annotations"]))
            print("Labels in progress!")
            for i in tqdm(range(0, len(data_original["images"]))):
                data_new["images"][i]['file_name'] = data_original["images"][i]['file_name'][15:-5] + ".png"
                data_new["images"][i]['id'] = int(data_original["images"][i]['id'][15:-1])
                for j in range(0, len(data_new["annotations"])):
                    if (data_new["images"][i]['id']) == int(data_original["annotations"][j]['image_id'][15:-1]):
                        data_new["annotations"][j]['image_id'] = data_new["images"][i]['id']
                time.sleep(0.2)
            time.sleep(0.5)
            print("New Annotations Ready For Fusion!")
            with open(self.gt_path, 'w') as _f:
                json.dump(data_new, _f)
                _f.close()

    # **************************************************************************
    def main(self):
        if self.init:
            self._Edit_Gt_Label()
        for file in glob.glob(self.json_path+"/*.json"):
            data = self._Open_Json(file)
            self._json_2_Csv(file[6:-9] + "csv", data)

    if __name__ == "__main__":
        main()
