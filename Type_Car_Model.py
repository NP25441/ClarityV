from keras.models import load_model
import cv2
import numpy as np

class Type_Car_Model(object):
    def __init__ (self): 
        pass
    
    
    def type_car_model(self, full_path, model_path):
        model = load_model(model_path)
        img = cv2.imread(full_path)
        img = cv2.resize(img, (150, 150))
        img = np.array([img])
        # classes = ['Sedan', 'Van', 'Pickup', 'Truck', 'Unknown']
        classes = ['รถเก๋ง', 'รถตู้', 'รถกระบะ', 'รถบรรทุก', 'ไม่ระบุประเภท']
        type = classes[np.argmax(model.predict(img))]
        
        print('Detect Type Car : ',type)
        
        return type
        
    


