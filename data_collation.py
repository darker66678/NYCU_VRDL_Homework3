import json
import os
import shutil

# deal with train_data
path = r'./nucleus/train/'
train_imgs = os.listdir(path)
train_destination = r'./mmdetection/nucleus/imgs/train/'

if not os.path.isdir(train_destination):
    os.makedirs(train_destination)

for img in train_imgs:
    file = img+'.png'
    shutil.copy(path+img+"/images/"+file, train_destination+file)

# deal with test_data
path = r'./nucleus/test/'
test_destination = r'./mmdetection/nucleus/imgs/test/'

if not os.path.isdir(test_destination):
    os.makedirs(test_destination)

for img in os.listdir(path):

    if img[-3:] == "png":
        shutil.copy(path+img, test_destination+img)

path = r'./nucleus/test_img_ids.json'
with open(path)as f:
    data = json.load(f)
test_json = {'images': data,
             'categories': [{"supercategory": "nucleus",
                            "id": 1,
                             "name": "nucleus"}]
             }
with open("./mmdetection/nucleus/{}.json".format("test_img_ids"), "w") as outfile:
    json.dump(test_json, outfile, indent=4)

print("collation finish!")
