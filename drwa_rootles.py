# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:58:42 2023

@author: lenovo
"""

import nibabel as nib
import matplotlib.pyplot as plt
import cv2
import os
from matplotlib import pyplot
import pydicom
import numpy as np
import dicom2nifti
import skimage

nii_file = 'YOUR_DATA_PATH/Segmentation_6-Segment_1-label_1.nii.gz'
seg_file = 'YOUR_DATA_PATH/t2_de3d_we_sag_p2_iso_0005_seg.nii.gz'
nii_img =  nib.load(nii_file)
seg_img = nib.load(seg_file)
nii_data = nii_img.get_data()
seg_data = seg_img.get_data()
seg_affine = seg_img.affine.copy()
seg_hdr = seg_img.header.copy()

assert nii_data.shape == seg_data.shape

for i in range(nii_data.shape[1]):
    if np.max(nii_data[:,i,:]) > 0:
        print(i)
        print(np.where(nii_data[:,i,:] == np.max(nii_data[:,i,:])))
        pyplot.imshow(nii_data[:,i,:])
        pyplot.imshow(seg_data[:,i,:])
        pyplot.show
        
        img = nii_data[:,i,:]
        img = img.squeeze()
        img = cv2.convertScaleAbs(img)
        # 阈值分割图像
        _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
        
        # 连通组件分析
        n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
        
        # 为每个连通组件绘制矩形框和编号
        for j in range(1, n_labels):
            x, y, w, h, area = stats[j]
            cx, cy = centroids[j]
            if cy < img.shape[0] / 2 + 4:
                cv2.line(img, (int(cx), int(cy)), (int(cx - 10), int(cy - 30)), (255, 255, 255), 1)
            else:
                cv2.line(img, (int(cx), int(cy)), (int(cx - 10), int(cy + 30)), (255, 255, 255), 1)
        
        for k in range(img.shape[0]):
            for l in range(img.shape[1]):
                if img[k,l] != 0:
                    seg_data[k,i,l] = 1
        # pyplot.imshow(img)
        # pyplot.show

new_nii = nib.Nifti1Image(seg_data, seg_affine, seg_hdr)
savename = 'new_spine.nii.gz'
nib.save(new_nii, 'E:/' + savename)

        
        