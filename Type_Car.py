from keras.models import load_model
import cv2
import numpy as np

class Type_Car_Model(object):
    def __inf__ (self):     
        pass
    
    
    def type_car_model(self,img):
        model = load_model('model_car(VGG16)\car_model.h5')
        img = cv2.resize(img, (150, 150))
        img = np.array([img])
        classes = ['รถเก๋ง', 'รถตู้', 'รถกระบะ', 'รถบรรทุก', 'ไม่ใช่รถ']
        print(classes[np.argmax(model.predict(img))])
        # print("Error: Cannot load model")
        # model.summary()
        # print("Loaded Model from disk")

        # # compile and evaluate loaded model

        # print(model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy']))
        
    


