#รวมทุกฟังก์ชัน

from Car_Detect import *
from Color import * # ทดสอบแล้ว
from Tesseract import * # ทดสอบผ่านแล้ว
from Type_Car import * # ทดสอบผ่านแล้ว
import os
import sys
import requests
from datetime import datetime,date
import pytz

# ตำแหน่ง API
url = "https://10f5-58-8-64-175.ap.ngrok.io/plates/create"

# ตั้งค่า Timezone
tz = pytz.timezone('Asia/Bangkok')

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
index_0 = 00
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
                    ocr_license_plate = ocr_plate.tessract_detect(full_path)
                # แสดงค่าที่ Error
                except Exception as e:
                  ocr_license_plate = ("Unknown License Plate")
                  # print("Error: Detect Plate")
                  
                # ดัก Error แล้วเด้งออกจากโปรแกรม
                try:
                    #รัน OCR Detect Plate
                    ocr_city_plate = ocr_plate.tessract_detect(full_path)
                # แสดงค่าที่ Error
                except Exception as e:
                  ocr_city_plate = ("Unknown City Plate")
                  # print("Error: Detect Plate")
                
                # ดัก Error แล้วเด้งออกจากโปรแกรม  
                try:
                    # รัน Detect Color
                    color = color_car.color_detect(full_path)
                # แสดงค่าที่ Error 
                except Exception as e:
                  print("Error: Detect Color")
                    
                
                # ตั้งค่าเวลา
                time_tz = datetime.now(tz)
                current_time = time_tz.strftime("%H.%M.%S")
                # ตั้งค่าวันที่
                date_tz = date.today(tz)
                current_date = date_tz.strftime("%d.%m.%Y")
                
                # แสดงค่าที่ได้ทั้งหมด
                print("ocr",ocr_license_plate)
                print("ocr",ocr_city_plate)
                print("type",type)
                print("color",color)
                print("time",current_time)
                print("date",current_date)
                os.rename (full_path,f'Snapshot-Data\{index_0}{index}_{ocr_license_plate}_{ocr_city_plate}_{type}_{color}_{current_time}_{current_date}.jpg')
                
                headers = {'Accept': 'application/json',
                            'content-type': 'application/json',
                            'Access-Control_Allow_Origin': '*',}
                
                myobj = { 'id': index,
                          'license_plate': ocr_license_plate,
                          'city': ocr_city_plate,
                          'vehicle':type,
                          'color': color,
                          'time': current_time,
                          'date': current_date,
                        }
                
                post = requests.post(url,json=myobj,headers=headers)
                
                print(post.status_code)
                print(post.json())
                index += 1
                
    
    # แสดงค่าที่ Error            
    except Exception as e:
                  print(str(e))