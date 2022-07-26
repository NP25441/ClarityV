from test_00 import *
import cv2
from keras.models import load_model

model = load_model('model_car')
print(model.summary())

img_path = r'Test_data\image.jpg'

classFile = 'coco.names'
detector = Detector()
detector.readClasses(classFile)
detector.predictImage(img_path)