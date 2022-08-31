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
        
        # if type == "Unknown":
        #     type = "ไม่ใช่รถยนต์"
            
        # elif type == "Sedan":
        #     type = "รถเก๋ง"
            
        # elif type == "Van":
        #     type = "รถตู้"
            
        # elif type == "Pickup":
        #     type = "รถกระบะ"
            
        # elif type == "Truck":
        #     type = "รถบรรทุก"
        
        return type
        # print("Error: Cannot load model")
        # model.summary()
        # print("Loaded Model from disk")

        # # compile and evaluate loaded model

        # print(model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy']))
        
    


