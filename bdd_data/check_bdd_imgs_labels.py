
# 检查下label的txt文件是否有对应的Img文件
# Make sure that image matches the label one-to-one

import glob, os, shutil

'''
Sometimes your image data set might not match with your label data set.
This code does the folowing
(1) Go through your image data set
(2) Search if the corresponding label file exist in the label data set. 
(3) If not, remove current image
'''


def copy_filter(label_dir,image_dir,target_dir_images,target_dir_labels):
    for image in os.listdir(image_dir):
        if image.endswith('jpg'):
            image_name = os.path.splitext(image)[0]

            # Corresponding label file name
            label_name = image_name + '.txt'
            image_path = image_dir + '/' + image_name + '.jpg'
            if os.path.isfile(label_dir + '/' + label_name) == False:
                print(" -- DELETE IMAGE [Label file not found -- ]")
                
                # print(image_path)
                # os.remove(image_path)
            else:
                target_images=target_dir_images+ '/' + image_name + '.jpg'
                shutil.copy(image_path,target_dir_images )
                # print(" --COPY IMAGE "+target_images)


    for label in os.listdir(label_dir):
        if label.endswith('.txt'):
            label_name = os.path.splitext(label)[0]

            # Corresponding label file name
            image_name = label_name + '.jpg'
            label_path = label_dir + '/' + label_name + '.txt'
            if os.path.isfile(image_dir + '/' + image_name) == False:
                print(" -- DELETE LABEL [Image file not found -- ]")
                # print(label_path)
                # os.remove(label_path)
            else:
                target_labels=target_dir_labels+ '/' + label_name + '.txt'
                shutil.copy(label_path,target_labels )
                # print(" --COPY lABELS "+target_labels)

'''创建存储目录
mkdir -p bdd100k/images/trains
mkdir -p bdd100k/labels/trains
mkdir -p bdd100k/images/valids
mkdir -p bdd100k/labels/valids
'''

# 1 check training data, 原来是 69863
# label_dir = '../../bdd_data_archive/parsed/trains'
# image_dir = "../../bdd_data_archive/bdd100k/bdd100k/images/100k/train"
# target_dir_images="../../bdd_data_archive/images/trains"
# target_dir_labels="../../bdd_data_archive/labels/trains"
# copy_filter(label_dir,image_dir,target_dir_images,target_dir_labels)


# 2 check validating data， 原来是 10000
label_dir2 = '../../bdd_data_archive/parsed/valids'
image_dir2 = "../../bdd_data_archive/bdd100k/bdd100k/images/100k/val"
target_dir_images2="../../bdd_data_archive/images/valids"
target_dir_labels2="../../bdd_data_archive/labels/valids"
copy_filter(label_dir2,image_dir2,target_dir_images2,target_dir_labels2)

# 统计下数量
labels_list=glob.glob("../../bdd_data_archive/labels/trains"+"/"+"*.txt")
images_list=glob.glob("../../bdd_data_archive/images/trains"+"/"+"*.jpg")
print('train labels num:', len(labels_list))
print('train imgs num:', len(images_list))

labels_list2=glob.glob("../../bdd_data_archive/labels/valids"+"/"+"*.txt")
images_list2=glob.glob("../../bdd_data_archive/images/valids"+"/"+"*.jpg")
print('valid labels num:', len(labels_list2))
print('valid imgs num:', len(images_list2))