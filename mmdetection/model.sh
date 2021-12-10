if [ $1 == "train" ]; then
    python tools/train.py ./work_dirs/mask_rcnn_r101_fpn_2x_coco/mask_rcnn_r101_fpn_2x_coco.py
elif [ $1 == "test" ]; then
    python tools/test.py ./work_dirs/mask_rcnn_r101_fpn_2x_coco/mask_rcnn_r101_fpn_2x_coco.py $2  --format-only --options "jsonfile_prefix=./results"
elif [$1 =="show" ]; then
    python tools/test.py ./work_dirs/mask_rcnn_r101_fpn_2x_coco/mask_rcnn_r101_fpn_2x_coco.py $2  --show
fi

