_base_ = [
    './_base_/models/retinanet_r50_fpn.py',
    './_base_/datasets/coco_detection.py',
    './_base_/schedules/schedule_1x.py', './_base_/default_runtime.py'
]
model = dict(
    pretrained='open-mmlab://regnetx_3.2gf',
    backbone=dict(
        _delete_=True,
        type='RegNet',
        arch='regnetx_3.2gf',
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=True,
        style='pytorch'),
    neck=dict(
        type='FPN',
        in_channels=[96, 192, 432, 1008],
        out_channels=256,
        num_outs=5))
img_norm_cfg = dict(
    # The mean and std are used in PyCls when training RegNets
    mean=[103.53, 116.28, 123.675],
    std=[57.375, 57.12, 58.395],
    to_rgb=False)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(800, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(
        type='Albu',
        transforms=[
            dict(
                type='RandomBrightnessContrast',
                brightness_limit=0.1,
                contrast_limit=0.1,
                p=0.5)
        ],
        bbox_params=dict(
            type='BboxParams',
            format='coco',
            label_fields=['gt_labels'],
            min_visibility=0.3,
            filter_lost_elements=True),
        keymap=dict(img='image', gt_bboxes='bboxes')),
    dict(
        type='Normalize',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        to_rgb=True),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels'])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(320, 320),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img'])
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type='CocoDataset',
        ann_file='./new_dataset/new_train.json',
        img_prefix='./new_dataset/new_train/images/',
        pipeline=train_pipeline),
    val=dict(
        type='CocoDataset',
        ann_file='./new_dataset/new_val.json',
        img_prefix='./new_dataset/new_val/images/',
        pipeline=test_pipeline),
    test=dict(
        type='CocoDataset',
        ann_file='./ground_truth/ground_truth.json',
        img_prefix='./test_images/',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.001)
optimizer_config = dict(grad_clip=None)
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[5, 10, 15, 25, 35])
runner = dict(type='EpochBasedRunner', max_epochs=40)
checkpoint_config = dict(interval=1)
log_config = dict(interval=100, hooks=[dict(type='TextLoggerHook')])
custom_hooks = [dict(type='NumClassCheckHook')]
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = './retinanet_regnetx-3.2GF_fpn_1x_coco_20200520_163141-cb1509e8.pth'
resume_from = None
workflow = [('train', 1)]
work_dir = './retinanet_regnetx-3.2GF_fpn_1x'
seed = 0
gpu_ids = range(0, 1)
total_epochs = 40
