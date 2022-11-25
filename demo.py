''' 
test torch-gpu env
'''

import torch
from torch.backends import cudnn 

a = torch.cuda.is_available()
print(a)
ngpu= 1
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
print(device)
print(torch.cuda.get_device_name(0))
print(torch.rand(3,3).cuda())


print("判断是否安装了cuDNN")
print(cudnn.is_available())  #返回True则说明已经安装了cuDNN

''' 测试tf-gpu
import tensorflow as tf
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
print(tf.test.is_gpu_available())
'''