_base_ = [
    './_base_/datasets/coco_detection.py',
    './_base_/schedules/schedule_1x.py', './_base_/default_runtime.py'
]
model = dict(
    type='PAA',  # detection algoritmasının tanımlanması
    pretrained='torchvision://resnet50',  # sınıflandırıcı alt ağın tanımlandırılması
    backbone=dict(  # sınıflandırocoın ağın konfigüreasyonu
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),  # normalizasyon tipinin belirlenmesi . batch normalizayosn
        norm_eval=True,
        style='pytorch'),  # pytorch yada caffe olarak apılanrıılması
    neck=dict(
        type='FPN',  #
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        start_level=1,
        add_extra_convs='on_output',
        num_outs=5),
    bbox_head=dict(  # bbox head belirlenmesi
        type='PAAHead',
        reg_decoded_bbox=True,
        score_voting=True,
        topk=9,
        num_classes=1,
        in_channels=256,
        stacked_convs=4,
        feat_channels=256,
        anchor_generator=dict(
            type='AnchorGenerator',
            ratios=[1.0],
            octave_base_scale=8,
            scales_per_octave=1,
            strides=[8, 16, 32, 64, 128]),
        bbox_coder=dict(
            type='DeltaXYWHBBoxCoder',
            target_means=[.0, .0, .0, .0],
            target_stds=[0.1, 0.1, 0.2, 0.2]),
        loss_cls=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=2.0,
            alpha=0.25,
            loss_weight=1.0),
        loss_bbox=dict(type='GIoULoss', loss_weight=1.3),
        loss_centerness=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=0.5)),

    # training and testing settings
    train_cfg=dict(
        assigner=dict(
            type='MaxIoUAssigner',
            pos_iou_thr=0.1,
            neg_iou_thr=0.1,
            min_pos_iou=0,
            ignore_iof_thr=-1),
        allowed_border=-1,
        pos_weight=-1,
        debug=False),
    test_cfg=dict(
        nms_pre=1000,
        min_bbox_size=0,
        score_thr=0.05,
        nms=dict(type='nms', iou_threshold=0.6),
        max_per_img=100))
# # use ResNeSt img_norm
img_norm_cfg = dict(
    mean=[123.68, 116.779, 103.939], std=[58.393, 57.12, 57.375], to_rgb=True)
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
            dict(
                type='Normalize',
                mean=[123.675, 116.28, 103.53],
                std=[58.395, 57.12, 57.375],
                to_rgb=True),
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
        pipeline=train_pipeline,
        data_root=''),
    val=dict(
        type='CocoDataset',
        ann_file='./new_dataset/new_val.json',
        img_prefix='./new_dataset/new_val/images/',
        pipeline=test_pipeline,
        data_root=''),
    test=dict(
        type='CocoDataset',
        ann_file='./ground_truth/ground_truth.json',
        img_prefix='./test_images/',
        pipeline=test_pipeline,
        data_root=''))
evaluation = dict(interval=1, metric='bbox')
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.001)
optimizer_config = dict(grad_clip=None)
lr_config = dict(
    policy='step',
    warmup=None,
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[5, 10, 15, 25, 35])
runner = dict(type='EpochBasedRunner', max_epochs=40)
checkpoint_config = dict(interval=1)
log_config = dict(interval=100, hooks=[dict(type='TextLoggerHook')])
custom_hooks = [dict(type='NumClassCheckHook')]
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = './paa_r50_fpn_1.5x_coco_20200823-805d6078.pth'
resume_from = None
workflow = [('train', 1)]
work_dir = './paa_r50_fpn_1x_coco'
seed = 0
gpu_ids = range(0, 1)
total_epochs = 40
