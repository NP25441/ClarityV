class Type_Car_Img(object):
    def __init__ (self): 
        pass
    
    
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
        
        print('Type Img Car : ',type_car_img)
        
        return type_car_img