from keras.models import load_model
import mrcnn
import mrcnn.config
import mrcnn.model
import mrcnn.visualize
import cv2
import os

#ประเภทที่มี Model
Class_Car = ['Sedan', 'Van', 'Pickup', 'Truck', 'Unknow']

#นำเข้า Model
model = load_model('D:\Develop\Senior_Project\ClarityV\model_car')
print(model.summary())


class SimpleConfig(mrcnn.config.Config):
    NAME = "coco_inference"
    
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    NUM_CLASSES = len(Class_Car)

model = mrcnn.model.MaskRCNN(mode="inference", 
                             config=SimpleConfig(),
                             model_dir=os.getcwd())

model.load_weights(filepath="mask_rcnn_coco.h5", 
                   by_name=True)


image = cv2.imread("D:\Develop\Senior_Project\ClarityV\Test_data\2DCX30J18R7X.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

r = model.detect([image], verbose=0)

r = r[0]

mrcnn.visualize.display_instances(image=image, 
                                  boxes=r['rois'], 
                                  masks=r['masks'], 
                                  class_ids=r['class_ids'], 
                                  class_names=Class_Car, 
                                  scores=r['scores'])