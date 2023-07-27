# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:59:32 2023

@author: lenovo
"""

from spinalcordtoolbox.scripts import sct_deepseg_gm_module
from spinalcordtoolbox.scripts import sct_deepseg_sc_module
from spinalcordtoolbox.scripts import sct_label_vertebrae_module

import nibabel as nib
import matplotlib.pyplot as plt
import cv2
import numpy as np

# # # segement gray matter
# input_file = 'E:/t2_space_cor_iso_myelo_ZOOMit_0009_1.nii.gz'
input_file = 'E:/影像中心数据/JIA FUMIN^Spine MRI_20230306_173718.359000/001nii/t2_space_cor_iso_myelo_ZOOMit_0009_1.nii.gz'
# # thr_gm = None
# # sct_deepseg_gm_module.run_main(input_file, thr_gm)

# segement spinal cord
thr_sc = 99.0
centerll = 'svm' # choices=('svm', 'cnn', 'viewer', 'file')
type_c_sc = 't2' # choices=('t1', 't2', 't2s', 'dwi')
dimen = '2d' #choices=('2d', '3d')
seg_file = sct_deepseg_sc_module.run_main(input_file, type_c_sc, dimen, thr_sc, centerll)

# type_c_label = 't2'
# sct_label_vertebrae_module.run_main(input_file, seg_file, type_c_label)


# seg_file = 'E:/影像中心数据/JIA FUMIN^Spine MRI_20230329_135927.431000/006nii/t2_de3d_we_sag_p2_iso_0005_seg.nii.gz'
# label_file = 'E:/SCT/zips/spinalcordtoolbox-master/spinalcordtoolbox-master/data/sct_example_data/t2/t2_seg_labeled.nii.gz'
# nii_raw_img =  nib.load(input_file)
# nii_seg_img = nib.load(seg_file)
# nii_labeled_img = nib.load(label_file)

# nii_raw_img_data = nii_raw_img.get_data()
# nii_seg_img_data = nii_seg_img.get_data()
# nii_label_img_data = nii_labeled_img.get_data()

# nii_seg_affine = nii_seg_img.affine.copy()
# nii_seg_hdr = nii_seg_img.header.copy()

# spinal_data = np.zeros((nii_seg_img_data.shape[0],nii_seg_img_data.shape[1],nii_seg_img_data.shape[2]))
# seg_smooth_data = np.zeros((nii_seg_img_data.shape[0],nii_seg_img_data.shape[1],nii_seg_img_data.shape[2]))
# csf_spine_data = np.zeros((nii_seg_img_data.shape[0],nii_seg_img_data.shape[1],nii_seg_img_data.shape[2]))
# csf_data = np.zeros((nii_seg_img_data.shape[0],nii_seg_img_data.shape[1],nii_seg_img_data.shape[2]))

# assert nii_raw_img_data.shape == nii_seg_img_data.shape
# b = np.nonzero(nii_seg_img_data)
# spinal_data[b] = nii_raw_img_data[b]
                           
# kernel = (3,3) 
# kernel_csf = (5,5)
# # plt.plot(nii_img_data[:,:,2]) #矢状面，冠状面，水平面
# # plt.subplot(1, 3, 1).imshow(nii_seg_img_data[30,:,:])
# # plt.subplot(1, 3, 2).imshow(spinal_data[30,:,:])

# for i in range(nii_seg_img_data.shape[0]):
#     tmp_img = spinal_data[i,:,:]
    
#     # seg_smooth_data[i,:,:] =  cv2.medianBlur(np.uint8(tmp_img),5)
    
#     seg_smooth_data[i,:,:] =  cv2.GaussianBlur(tmp_img,kernel,0,0)
#     csf_spine_data[i,:,:] = cv2.GaussianBlur(tmp_img,kernel_csf,0,0)

# for j in range(nii_seg_img_data.shape[1]):
#     tmp_img = seg_smooth_data[:,j,:]
    
#     # seg_smooth_data[:,j,:] =  cv2.medianBlur(np.uint8(tmp_img),5)
    
#     seg_smooth_data[:,j,:] =  cv2.GaussianBlur(tmp_img,kernel,0,0)
#     csf_spine_data[:,j,:] = cv2.GaussianBlur(tmp_img,kernel_csf,0,0)
    
# for k in range((nii_seg_img_data.shape[2])):
#     tmp_img = seg_smooth_data[:,:,k]
    
#     # seg_smooth_data[:,:,k] =  cv2.medianBlur(np.uint8(tmp_img),5)
    
#     seg_smooth_data[:,:,k] =  cv2.GaussianBlur(tmp_img,kernel,0,0)
#     csf_spine_data[:,:,k] = cv2.GaussianBlur(tmp_img,kernel_csf,0,0)
    
# # plt.close
# new_nii_seg_img = nib.Nifti1Image(seg_smooth_data, nii_seg_affine, nii_seg_hdr)
# nib.save(new_nii_seg_img, 'E:/' + 'new_seg2.nii.gz')

# for ii in range(nii_seg_img_data.shape[0]):
#     for jj in range(nii_seg_img_data.shape[1]):
#         for kk in range((nii_seg_img_data.shape[2])):
#                         if (seg_smooth_data[ii,jj,kk] == 0) & (csf_spine_data[ii,jj,kk] != 0):
#                             csf_data[ii,jj,kk] = csf_spine_data[ii,jj,kk]
# csf_nii_seg_img = nib.Nifti1Image(csf_data, nii_seg_affine, nii_seg_hdr)
# nib.save(csf_nii_seg_img, 'E:/' + 'csf_seg.nii.gz')

