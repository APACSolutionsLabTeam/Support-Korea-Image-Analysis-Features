# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 01:07:08 2021

@author: ZSPANIYA
"""
import cv2

testImage = cv2.imread(".\\Input\\testImage.jpg", 0)
height, width = testImage.shape[:2]
testImageSum = 0
testImageSumSquare = 0
for i in range(0, height):
    for j in range(0, width):
        ## Intensity Sum of Channel
        testImageSum = testImageSum+float(testImage[i][j])
        ## Intensity Sum Squares of Channel
        testImageSumSquare = testImageSumSquare + (float(testImage[i][j])*float(testImage[i][j]))
        
print('testImageSum', testImageSum)  
print('testImageSumSquare', testImageSumSquare)       
  