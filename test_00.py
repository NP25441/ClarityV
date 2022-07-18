import cv2
import os
import time
import tensorflow as tf
import numpy as np
from keras.models import load_model

from tensorflow.python.keras.utils.data_utils import get_file

np.random.seed(123)

model = load_model('model_car')


class Detector:
    def __inf__ (self):
        pass
    
    def readClasses(self, classesFilePath):
        with open(classesFilePath, 'r') as f:
            self.classesList = f.read().splitlines()
            
        self.colorList = np.random.uniform(low = 0, high = 255, size = (len(self.classesList), 3))
        
        print(len(self.classesList), len(self.colorList))
        
      
    def createBoundingBox(self, img):
        model = load_model('model_car')
        # model = model.load_weights('model_car\tmp\checkpoint')
        inputTensor = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
        inputTensor = tf.convert_to_tensor(inputTensor, dtype = tf.uint8)
        inputTensor = inputTensor[tf.newaxis, ...]
        
        detections = self.model(inputTensor)
        
        bboxs = detections['detection_boxes'][0].numpy()
        classIndexes = detections['detection_classes'][0].numpy().astype(np.int32)
        classScores = detections['detection_scores'][0].numpy()
        
        imH, imW, imC = img.shape
        
        if len(bboxs) !=0:
            for i in range(0, len(bboxs)):
                bboxs = tuple(bboxs[i].tolist())
                classConfidence = round(100*classScores[i])
                classIndex = classIndexes[i]
                
                classLabelText = self.classesList[classIndex]
                classColor = self.colorList[classIndex]
                
                displayText = '{} {}%'.format(classLabelText, classConfidence)
                
                ymin, xmin, ymax, xmax = bboxs
                
                print(ymin, ymax, xmin, xmax)
                break
            
    
    def predictImage(self, img_path):
        img = cv2.imread(img_path)
        
        self.createBoundingBox(img)
        
        # img = cv2.resize(img, (620,480) ) #ปรับขนาดรูปภาพ
        cv2.imshow("Image", img)#แสดงรูปภาพที่ได้จากการทำงาน
        cv2.waitKey(0)#รอการกดปุ่มเพื่อคืนค่า
        
        
    