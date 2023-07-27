# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:19:50 2023

@author: lenovo
"""

import nibabel as nib
import numpy as np
from scipy.ndimage import zoom
import SimpleITK as sitk
from scipy import ndimage

# 读取nii文件
img = nib.load('E:/人工脊髓/model/stl_m/NERVETRI_R.nii.gz')
voxel_size = img.header.get_zooms()
spacing = img.header['pixdim'][1:4]

data = img.get_fdata()
affine = img.affine
header = img.header

# dem = [2]
# target_spacing = spacing.copy()
# target_spacing *= 2
# zoom_factor = np.array(header['pixdim'][1:4]) / np.array(target_spacing)
# data_reconstructed = zoom(data, zoom_factor, order=1)
# # 体素重建，保持spacing一致
# for i in range(len(zoom_factor)):
#     factor = zoom_factor[i]
#     affine[i,i] /= factor

# affine[0:3, 3] *= (target_spacing / img.header.get_zooms()[:3]) 


# orig_min = np.min(data)
# orig_max = np.max(data)
# recon_min = np.min(data_reconstructed)
# recon_max = np.max(data_reconstructed)

# # 对重建后的数据进行灰度值线性变换
# # k = (orig_max - orig_min) / (recon_max - recon_min)
# # b = orig_min - k * recon_min
# # adj_data = k * data_reconstructed + b
# data_reconstructed[data_reconstructed != 0] = 1

# header['pixdim'][1:4] = [1,1,1]
# new_img = nib.Nifti1Image(data_reconstructed, affine=img.affine, header = img.header)

# # 保存新的nii文件
# nib.save(new_img, 'E:/人工脊髓/model/stl_m/NERVETRI_rescale.nii.gz')
