# -*- coding: utf-8 -*-
"""Utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KZinfMBV1F904PLoB1dpKtWhWtJe3PH7
"""

import cv2
from google.colab.patches import cv2_imshow
import pandas as pd
import os, json

def imShowScale(im,scale=10):
  imResize=cv2.resize(im,(int(im.shape[1]/scale),int(im.shape[0]/scale)))
  cv2_imshow(imResize)

def prepareExcelFile(rootPath,fileName):
  def add_name_and_commonPath_columns(data):
     data['name'] = data.iloc[:,0].map(lambda x : (((x.split('\\'))[-1]).split('.'))[0])
     data['commonPath'] = data.iloc[:,0].map(lambda x : '/'.join(((x.split('\\'))[-3:])) )
     return data

  filePath = os.path.join(rootPath,fileName)

  fileData = pd.read_excel(filePath, header=None,names=['path'])
  fileData= add_name_and_commonPath_columns(fileData)
  return fileData

def savePicture(rootPath,fileName,fileExtension,im):
  filePath = os.path.join(rootPath,fileName)
  filePath = os.path.join(filePath,fileExtension)
  if not os.path.isfile(filePath):
    print(filePath)
    cv2.imwrite(filePath,im)