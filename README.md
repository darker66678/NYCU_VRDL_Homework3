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
``` python data_collation.py``` Collate all the data 

``` python coco_trans.py.py ``` Convert mask img into json file of coco 
## Training
## Evaluation
## Pre-trained model
## Results
