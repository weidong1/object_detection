#-*-coding:utf-8-*-
# 把coco格式转换成yolo格式

# python3 coco2yolo.py --datasets COCO --img_path /home/iav/code/bdd100k_yolov5/bdd100k_images/bdd100k/images/100k/train --label labels/bdd100k_labels_images_det_coco_val.json --convert_output_path train_labels/ --img_type ".jpg" --manipast_path ./ --cls_list_file bdd100k.names

import os
from xml.etree.ElementTree import dump
import json
import pprint

import argparse

from Format import COCO,YOLO

def main(config):

    if config["datasets"] == "COCO":
        coco = COCO()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = coco.parse(config["label"])

        if flag == True:
            flag, data = yolo.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                        config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("COCO Parsing Result : {}, msg : {}".format(flag, data))

    else:
        print("Unkwon Datasets")

if __name__ == '__main__':

    # config ={
    #     "datasets": "COCO",
    #     "img_path": "../../bdd_data_archive/bdd100k/bdd100k/images/100k/train",
    #     "label": "../../bdd_data_archive/parsed/bdd100k_labels_images_det_coco_train.json",
    #     "img_type": ".jpg",
    #     "manipast_path": "./",
    #     "output_path": "../../bdd_data_archive/parsed/trains/",
    #     "cls_list": "./bdd100k.names",
    # }

 
    config ={
        "datasets": "COCO",
        "img_path": "../../bdd_data_archive/bdd100k/bdd100k/images/100k/val",
        "label": "../../bdd_data_archive/parsed/bdd100k_labels_images_det_coco_val.json",
        "img_type": ".jpg",
        "manipast_path": "./",
        "output_path": "../../bdd_data_archive/parsed/valids",
        "cls_list": "./bdd100k.names",
    }

    main(config)