rm results.bbox.json
mv results.segm.json answer.json
zip $1 answer.json
rm answer.json
file=$1'.zip'
mv $file ./work_dirs/mask_rcnn_r101_fpn_2x_coco/results