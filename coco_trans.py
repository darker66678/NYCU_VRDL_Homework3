import glob
import pandas as pd
import os
import json
import cv2
from pycocotools import mask as cocomask

category_ids = {
    "nucleus": 1,
}


def annToRLE(segm, i_w, i_h):
    h, w = i_h, i_w
    if type(segm) == list:
        rles = cocomask.frPyObjects(segm, h, w)
        rle = cocomask.merge(rles)
    elif type(segm['counts']) == list:
        rle = cocomask.frPyObjects(segm, h, w)
    else:
        rle = ann['segmentation']
    return rle


def binary_mask_to_rle(binary_mask):
    rle = {'counts': [], 'size': list(binary_mask.shape)}
    counts = rle.get('counts')
    last_elem = 0
    running_length = 0
    for i, elem in enumerate(binary_mask.ravel(order='F')):
        if elem == last_elem:
            pass
        else:
            counts.append(running_length)
            running_length = 0
            last_elem = elem
        running_length += 1
    counts.append(running_length)
    return rle


def annotation_format(img, image_id, category_id, annotation_id):
    rle = binary_mask_to_rle(img)

    area_rle = cocomask.frPyObjects(rle, rle['size'][0], rle['size'][1])
    area = float(cocomask.area(area_rle))
    area_rle['counts'] = area_rle['counts'].decode('ascii')
    annotation = {
        "segmentation": area_rle,
        "area": area,
        "iscrowd": 0,
        "image_id": image_id,
        'bbox': list(cocomask.toBbox(area_rle)),
        "category_id": category_id,
        "id": annotation_id
    }
    return annotation


def images_annotations_info(maskpath, file, image_id, annotations, images, annotation_id):
    original_file_name = file + ".png"
    print(original_file_name)
    w = 1000
    h = 1000
    category_id = 1

    image = create_image_annotation(original_file_name, w, h, image_id)
    images.append(image)

    for mask_image in glob.glob(maskpath + "*.png"):
        img = cv2.imread(mask_image, cv2.THRESH_BINARY)
        annotation = annotation_format(
            img, image_id, category_id, annotation_id)
        annotations.append(annotation)
        annotation_id = annotation_id+1
    return images, annotations, annotation_id


def get_coco_json_format():
    # Standard COCO format
    coco_format = {
        "info": {},
        "licenses": [],
        "images": [{}],
        "categories": [{}],
        "annotations": [{}]
    }

    return coco_format


def create_category_annotation(category_dict):
    category_list = []

    for key, value in category_dict.items():
        category = {
            "supercategory": key,
            "id": value,
            "name": key
        }
        category_list.append(category)

    return category_list


def create_image_annotation(file_name, width, height, image_id):
    images = {
        "file_name": file_name,
        "height": height,
        "width": width,
        "id": image_id
    }

    return images


if __name__ == "__main__":
    # Get the standard COCO JSON format
    path = './nucleus/train'
    allFileList = os.listdir(path)
    print("preparing train.json")
    image_id = 1
    annotation_id = 1
    coco_format = get_coco_json_format()
    coco_format["categories"] = create_category_annotation(category_ids)
    coco_format["images"] = []
    coco_format["annotations"] = []

    for file in allFileList:
        mask_path = f'./nucleus/train/{file}/masks/'
        coco_format["images"], coco_format["annotations"], annotation_id = images_annotations_info(
            mask_path, file, image_id, coco_format["annotations"], coco_format["images"], annotation_id)

        image_id = image_id+1

    with open("./mmdetection/nucleus/{}.json".format("train"), "w") as outfile:
        json.dump(coco_format, outfile, indent=4)
        print("finish!!")

    # validation data
    print("preparing val.json")
    image_id = 1
    annotation_id = 1
    coco_format = get_coco_json_format()
    coco_format["categories"] = create_category_annotation(category_ids)
    coco_format["images"] = []
    coco_format["annotations"] = []

    file = allFileList[-1]
    mask_path = f'./nucleus/train/{file}/masks/'
    coco_format["images"], coco_format["annotations"], annotation_id = images_annotations_info(
        mask_path, file, image_id, coco_format["annotations"], coco_format["images"], annotation_id)
    image_id = image_id+1

    with open("./mmdetection/nucleus/{}.json".format("val"), "w") as outfile:
        json.dump(coco_format, outfile, indent=4)
        print("finish!!")
