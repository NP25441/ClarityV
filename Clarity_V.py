#รวมทุกฟังก์ชัน

from Car_Detect import *
from Color import * # ทดสอบแล้ว
from Tesseract import * # ทดสอบผ่านแล้ว
from Type_Car import * # ทดสอบผ่านแล้ว
import os
import sys

# กำหนดตำแหน่งของไฟล์วิดีโอ
cap = cv2.VideoCapture('Test_data\Video-3.mp4')
# กำหนดตำแหน่งของโมเดล
model_path = 'model_car(VGG16)\car_model.h5'

#ตำแหน่งที่จะเก็บข้อมูล
path       = "Snapshot-Data"

# เรียกใช้ class ของตัวเอง
car_detection = Car_Detection()
type_car = Type_Car_Model()
ocr_plate = Tessract_Detect()
color_car = Color_Detect()

# ดัก Error แล้วเด้งออกจากโปรแกรม
try:
    # อ่านไฟล์วิดีโอที่ตรวจจับ Detect
    car_detection.car_detection(cap)
# แสดงค่าที่ Error
except Exception as e:
    print("Error: Cannot read video file")
index = 1
#วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
for images in os.listdir(path):
    # ดัก Error แล้วเด้งออกจากโปรแกรม
    try:
        #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
        if (images.endswith(".jpg")):
              # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
                full_path = path + "\\" + str(images)
                
                # ดัก Error แล้วเด้งออกจากโปรแกรม
                try:
                    #รัน Model Detect Car
                    type = type_car.type_car_model(model_path,full_path)
                # แสดงค่าที่ Error
                except Exception as e:
                  print("Error: Cannot load model")
                
                # ดัก Error แล้วเด้งออกจากโปรแกรม
                try:
                    #รัน OCR Detect Plate
                    ocr = ocr_plate.tessract_detect(full_path)
                # แสดงค่าที่ Error
                except Exception as e:
                  ocr = ("Unknown License Plate")
                  # print("Error: Detect Plate")
                
                # ดัก Error แล้วเด้งออกจากโปรแกรม  
                try:
                    # รัน Detect Color
                    color = color_car.color_detect(full_path)
                # แสดงค่าที่ Error 
                except Exception as e:
                  print("Error: Detect Color")
                    
                
                    
                print("type",type)
                print("ocr",ocr)
                print("color",color)
                os.rename (full_path,f'Snapshot-Data\{index}_{ocr}_{type}_{color}.jpg')
                index += 1
    
    # แสดงค่าที่ Error            
    except Exception as e:
                  print(str(e))