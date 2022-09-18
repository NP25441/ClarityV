#รวมทุกฟังก์ชันที่เรียกใช้
import json
from Car_Detect import * # ทดสอบผ่านแล้ว
from Color import * # ทดสอบแล้ว
from Tesseract import * # ทดสอบผ่านแล้ว
from Type_Car import * # ทดสอบผ่านแล้ว
from GDrive import * # ทดสอบผ่านแล้ว
import os
import sys
import requests
from datetime import datetime,date
import pytz
import natsort
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import pandas as pd

# กำหนดค่าเริ่มต้น

# ตำแหน่ง API
plate_url = "https://d720-2001-fb1-108-c52a-4408-4534-fe52-ffff.ap.ngrok.io"

# ตั้งค่า Timezone
tz = pytz.timezone('Asia/Bangkok')

# กำหนดตำแหน่งของไฟล์วิดีโอ
cap = cv2.VideoCapture('Test_data\Video-3.mp4')

# กำหนดตำแหน่งของโมเดล
model_path = 'model_car(VGG16)\car_model.h5'

#ตำแหน่งที่จะเก็บข้อมูล
path = "Snapshot-Data"


# เรียกใช้ฟังก์ชันที่เขียนไว้เป็น Class
# -------------------------------------

# เรียกใช้ class ของ Car_Detect
car_detection = Car_Detection()

# เรียกใช้ class ของ Type_Car
type_car = Type_Car_Model()

# เรียกใช้ class ของ Tesseract
ocr_plate = Tessract_Detect()

# เรียกใช้ class ของ Color
color_car = Color_Detect()

# เรียกใช้ class ของ GDrive
gdrive_img_path = GDrive_Img()


# กระบวนการที่ 1 ของระบบ อ่านวิดีโอ และ ตรวจจับรถ
# -------------------------------------

# ดัก Error ของารอ่านวิดีโอ
try:
    # อ่านไฟล์วิดีโอ โดยใช้ Model ของ MobileNet
    car_detection.car_detection(cap)
    
# แสดงข้อมูลที่ Error 
except Exception as e:
    print("Error: Read Video ")


#  ตั้งค่าเริ่มต้นในการไล่ลำดับของการนับข้อมูล
index = 1

# ไว้สำหรับเป็นข้อมูลทั้งหมด เพื่อนำมาเรียงข้อมูลอีกครั้ง
list_path = []


# กระบวนการที่ 2 ของระบบ อ่านตำแหน่งของรูปภาพที่ตรวจจับได้และจัดเก็บใหม่
# -------------------------------------

#วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
for images in os.listdir(path):
    # ดัก Error ในการอ่านตำแหน่งของไฟล์
    try:
        #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
        if (images.endswith(".jpg")):
              
              # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
              full_path = path + "\\" + str(images)
              
              # เพิ่มข้อมูลไฟล์ภาพเข้าไปใน list
              list_path.append(full_path)
              
    # แสดงข้อมูลที่ Error             
    except Exception as e:
      print('Error: Read Image')
      

# กระบวนการที่ 3 ของระบบ เรียงลำดับของข้อมูลและเข้าสู่กระบวนการอื่นๆ
# -------------------------------------

# เรียงลำดับข้อมูลให้ถูกต้องแล้วดึงออกมาทีละค่า
for _i ,full_path_len in enumerate(natsort.natsorted(list_path)):
              
  # ดัก Error ของการตรวจจับประเภทรถ
  try:
      # เริ่มกระบวนการทำงานของ Model Detect Car
      type = type_car.type_car_model(model_path,full_path_len)
      
  # แสดงข้อมูลที่ Error 
  except Exception as e:
    print("Error: Cannot load model")
  
  
  # ดัก Error ของการจับ OCR ทะเบียนรถ
  try:
      # เริ่มกระบวนการทำงานของ OCR Detect Plate
      ocr_license_plate = ocr_plate.tessract_detect(full_path_len)
      
  # แสดงข้อมูลที่ Error 
  except Exception as e:
    ocr_license_plate = ("Unknown License Plate")
    # print("Error: Detect Plate")
  
    
  # ดัก Error ของการจับ OCR จังหวัด
  try:
      # เริ่มกระบวนการทำงานของ OCR Detect Plate
      ocr_city_plate = ocr_plate.tessract_detect(full_path_len)
      
  # แสดงข้อมูลที่ Error 
  except Exception as e:
    ocr_city_plate = ("Unknown City Plate")

  
  # ดัก Error ของการจับสีรถ
  try:
      # เริ่มกระบวนการทำงานของ Detect Color
      color = color_car.color_detect(full_path_len)
      
  # แสดงข้อมูลที่ Error 
  except Exception as e:
    print("Error: Detect Color")
      
  
  # ดัก Error ของการตั้งค่าเวลา และ วันที่
  try:
    # ตั้งค่าเวลา
    # กำหนดโซนเวลาและเวลาปัจจุบัน
    time_tz = datetime.now(tz)
    # กำหนดรูปแบบเวลา
    current_time = time_tz.strftime("%H.%M.%S")
    
    # ตั้งค่าวันที่
    # ตั้งค่าวันที่ปัจจุบัน
    date_tz = date.today()
    # กำหนดรูปแบบวันที่
    current_date = date_tz.strftime("%d.%m.%Y")
      
  # แสดงข้อมูลที่ Error 
  except Exception as e:
    print("Error: Detect Color")
    
  
  # กระบวนการที่ 4 ของระบบ เปลี่ยื่อไฟล์ให้ถูกต้องตรงกับข้อมูลที่ได้จากการตรวจจับ
  # -------------------------------------
  
  # ดักข้อผิดพลาดของการเปลี่ยนชื่อไฟล์
  try:
    # เปลี่ยนชื่อไฟล์
    os.rename (full_path_len,f'Snapshot-Data\{index}_{ocr_license_plate}_{ocr_city_plate}_{type}_{color}_{current_time}_{current_date}.jpg')
  
  # แสดงข้อมูลที่ Error  
  except Exception as e:
    print("Error: Rename File")
    
    
  # กระบวนการที่ 5 ของระบบ เปลี่ยื่อไฟล์ให้ถูกต้องตรงกับข้อมูลที่ได้จากการตรวจจับ
  # -------------------------------------
    
  # ดักข้อผิดพลาดอัพโหลดรูปภาพ
  try:
    # เริ่มกระบวนการทำงานของ Upload Image to Google Drive
    img_path = gdrive_img_path.gdrive_img(index,ocr_license_plate,ocr_city_plate,type,color,current_time,current_date)
  
  # แสดงข้อมูลที่ Error  
  except Exception as e:
    print("Error: Google Drive Upload")
    

  # แสดงข้อมูลทั้งหมดเพื่อตรวจสอบ
  
  # แสดงค่าที่ได้ทั้งหมด
  print("index: ",index)
  print("ocr: ",ocr_license_plate)
  print("ocr: ",ocr_city_plate)
  print("type: ",type)
  print("color: ",color)
  print("time: ",current_time)
  print("date: ",current_date)
  print ("path: ",img_path)
  
  
  # กระบวนการที่ 6 ของระบบ รวมข้อมูลทั้งหมดและส่งข้อมูลไป API
  # -------------------------------------
  
  # Header ของไฟล์ 
  headers = {'Accept': 'application/json', # รับค่าเป็น json
              'content-type': 'application/json', # ส่งค่าเป็น json
              'Access-Control_Allow_Origin': '*'} # ส่งค่าไปที่ทุกๆที่
  
  # เรียงลำดับของข้อมูลที่จะส่งไปยัง API
  detel_car = { 'id': index, # รหัสรถ
            'license_plate': ocr_license_plate, # ทะเบียนรถ
            'city': ocr_city_plate, # จังหวัด
            'vehicle':type, # ประเภทรถ
            'color': color, # สีรถ
            'time': current_time, # เวลา
            'date': current_date, # วันที่
            # 'img': img, # ภาพ
          }
  
  # ดักข้อผิดพลาดของ API
  try:
    # ส่งข้อมูลไปยัง API
    post_detel = requests.post(plate_url + '/plates/create',json=detel_car,headers=headers)
    # แสดงสถานะของ API
    print(post_detel.status_code)
    # แสดงข้อมูลที่ส่ง
    print(post_detel.json())
    
  # แสดงกระบวการที่ผิดพลาด
  except Exception as e:
    print("Error: API")
  
  # เพิ่มค่าของลำดับให้ทำงานได้เป็นลำดับที่ถูกต้อง
  index += 1