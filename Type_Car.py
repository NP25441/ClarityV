from keras.models import load_model
import cv2
import numpy as np

class Type_Car_Model(object):
    def __init__ (self): 
        pass
    
    
    def type_car_model(self, model_path, full_path):
        model = load_model(model_path)
        img = cv2.imread(full_path)
        img = cv2.resize(img, (150, 150))
        img = np.array([img])
        # classes = ['Sedan', 'Van', 'Pickup', 'Truck', 'Unknown']
        classes = ['รถเก๋ง', 'รถตู้', 'รถกระบะ', 'รถบรรทุก', 'ไม่ระบุประเภท']
        type = classes[np.argmax(model.predict(img))]
        
        print('Detect Type Car : ',type)
        
        # if type == "ไม่ใช่รถยนต์":
        #     type_car_img = "https://drive.google.com/uc?export=view&id=1N-V3IQfHfhLSa4Dxb_40rszynGpx2pTA"
            
        # elif type == "รถเก๋ง":
        #     type_car_img = "https://drive.google.com/uc?export=view&id=1yoeilpPSFxteT69EK4coS-jKBfrpIV5s"
            
        # elif type == "รถตู้":
        #     type_car_img = "https://drive.google.com/uc?export=view&id=1iXM_n23gGIIvLOURVFJDbrGDW3Q1zBsQ"
            
        # elif type == "รถกระบะ":
        #     type_car_img = "https://drive.google.com/uc?export=view&id=1ZZNT3KY6vZHHbCJVy_Lq5IIUSc0WVQ-5"
            
        # elif type == "รถบรรทุก":
        #     type_car_img = "https://drive.google.com/uc?export=view&id=1zLAy8XqQfOiDpMhEHoyA3m2ieZ06EMKV"
        
        return type
        # print("Error: Cannot load model")
        # model.summary()
        # print("Loaded Model from disk")

        # # compile and evaluate loaded model

        # print(model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy']))
        
    


