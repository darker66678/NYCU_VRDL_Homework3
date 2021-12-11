# NYCU_VRDL_Homework3
This is  Homework 3  of  VRDL  about Instance segmentation for necleus dataset

| ```cocoapi``` [cocoAPI](https://github.com/cocodataset/cocoapi) is a very powerful tool in Segmentation and Object detection

| ```mmdetection```  This is a reference project from [mmdetection](https://github.com/open-mmlab/mmdetection)

| --- ```model.sh```  Command of model

| --- ```sub.sh``` Command of zipping  ```answer.json```

| --- ```train_config``` Pretrain model and config file are put in here

| --- ```tools```

| ------ ```train.py``` Main training program

| ------ ```test.py``` Main inference program

| ```nucleus``` Training and testing datasets should be put in here

| ```coco_trans.py``` Program of Converting mask img 

| ```data_collation.py``` Shell script for data collation

| ```install.sh``` Shell script for installing
## Requirements
Using python 3.7 in Anaconda

```sh install.sh``` Install all the dependencies
## Data preprocessing
Download Nucleus dataset and put in ```nucleus``` folder

Run ``` python data_collation.py``` for Collation all the data 

Run ``` python coco_trans.py.py ``` for Converting mask img into json file of coco 
## Training
you must download pretrained [R-101-FPN](https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r101_fpn_2x_coco/mask_rcnn_r101_fpn_2x_coco_bbox_mAP-0.408__segm_mAP-0.366_20200505_071027-14b391c7.pth)  as backbone and put it in ```./mmdetection/traon_config``` folder

Run ```sh model.sh train``` for Training model
## Inference
Run ```sh model.sh test [.pth file]``` for inference

```.json``` file will be save in ```./mmdetection/```

you can run ```sh sub.sh``` for zipping file quickly
## Pre-trained model
[R-101-FPN](https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r101_fpn_2x_coco/mask_rcnn_r101_fpn_2x_coco_bbox_mAP-0.408__segm_mAP-0.366_20200505_071027-14b391c7.pth)  as backbone, put it in ```./mmdetection/traon_config``` folder

[Mask R-CNN-R-101-FPN](https://drive.google.com/file/d/1X2wAembLcyyN7CNhQJ1V1Z_cl4sBegJq/view?usp=sharing) is my model file, you can generate  prediction result after checking *Evaluation* part
## Results
|model name|mAP|
|---|--|
|Mask R-CNN-R-101-FPN (840*840) + RandomCrop (600 * 600) + anchor scale =8|0.24518 
|Mask R-CNN-R-101-FPN (840*840) + RandomCrop (600 * 600) + anchor scale =6|0.244608
|Mask R-CNN-R-101-FPN (640*640) + anchor scale =8 |0.221494
