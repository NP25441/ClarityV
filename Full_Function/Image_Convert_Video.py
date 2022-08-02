import cv2
import numpy as np
import os
import glob

# choose codec according to format needed
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('Image2Video/video.mp4', fourcc, 1, (720, 1080))

img_array = []
index = 1

# read_img = cv2.imread('Image2Video\img (1).png')
# read_img = cv2.resize(read_img, (720, 1080))

for images in glob.glob('Image2Video/*.png'):
    img = cv2.imread(images)
    img = cv2.resize(img, (1080, 720))
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    
    video = cv2.VideoWriter('video.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 60, size)
 
for i in range(len(img_array)):
    video.write(img_array[i])
video.release()
# cv2.imshow('test',read_img)
cv2.destroyAllWindows()