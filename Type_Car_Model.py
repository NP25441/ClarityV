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
        
      #   print('Detect Type Car : ',type)
        
        return type
    
    
    def type_car_img(self, type):
        
        # ตรวจสอบประเภทของรถ เพื่อส่ง Path ของรูปภาพไปแสดงผล Frontend
        if type == "ไม่ใช่รถยนต์":
              type_car_img = "https://drive.google.com/uc?export=view&id=1N-V3IQfHfhLSa4Dxb_40rszynGpx2pTA"
              
        elif type == "รถเก๋ง":
              type_car_img = "https://drive.google.com/uc?export=view&id=1yoeilpPSFxteT69EK4coS-jKBfrpIV5s"
            
        elif type == "รถตู้":
              type_car_img = "https://drive.google.com/uc?export=view&id=1iXM_n23gGIIvLOURVFJDbrGDW3Q1zBsQ"
            
        elif type == "รถกระบะ":
              type_car_img = "https://drive.google.com/uc?export=view&id=1ZZNT3KY6vZHHbCJVy_Lq5IIUSc0WVQ-5"
            
        elif type == "รถบรรทุก":
              type_car_img = "https://drive.google.com/uc?export=view&id=1zLAy8XqQfOiDpMhEHoyA3m2ieZ06EMKV"
        
      #   print('Type Img Car : ',type_car_img)
        
        return type_car_img
        
    


