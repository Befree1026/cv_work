import numpy as np
import os

separator  = os.sep
tp = []
gt = []
root = 'D:\python object\CASIAv2\CASIA 2.0 dataset\Tp\\'
root2 = 'D:\python object\CASIAv2\CASIA 2.0 groundtruth\\'
with open('D:\\python object\\CASIAv2\\CASIA 2.0 dataset\\Tp\\_list.txt', 'r', encoding='utf-8') as f:
        for data in f.readlines():
            data = data.strip('\n')
            data = root + data
            tp.append(data)
tp.remove(root + '_list.txt')
tp_t = tuple(tp)

with open('D:\\python object\\CASIAv2\\CASIA 2.0 dataset\\Tp\\_list.txt', 'r', encoding='utf-8') as f:
    for data2 in f.readlines():
        data2 = data2.strip('\n')
        if '.tif' in data2:
            data2 = data2.strip('.tif')
            data2 = root2 + data2 + '_gt' + '.png'
        if '.jpg' in data2:
            data2 = data2.strip('.jpg')
            data2 = root2 + data2 + '_gt' + '.png'
        gt.append(data2)
gt.remove('_list.txt')
gt_t = tuple(gt)

temple = []
train = []
for i in range(0, 5123):
    temple.append(tp[i])
    temple.append(gt[i])
    temple = tuple(temple)
    train.append(temple)
    temple = []
print(train)

np.save("train.npy", train)