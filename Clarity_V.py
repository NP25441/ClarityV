#รวมทุกฟังก์ชันที่เรียกใช้
import os, sys, requests, pytz, natsort, json # ทดสอบผ่านแล้ว
from Car_Detect import * # ทดสอบผ่านแล้ว
from Color import * # ทดสอบผ่านแล้ว
from Color_Flutter import * # ทดสอบผ่านแล้ว
from Tesseract import * # ทดสอบผ่านแล้ว
from Type_Car_Model import * # ทดสอบผ่านแล้ว
from Type_Car_Img import * # ทดสอบผ่านแล้ว
from GDrive import * # ทดสอบผ่านแล้ว
from datetime import datetime,date # ทดสอบผ่านแล้ว

# กำหนดค่าเริ่มต้น

# ตำแหน่ง API
plate_url = "https://706c-202-80-249-127.ap.ngrok.io"

# ตั้งค่า Timezone
tz = pytz.timezone('Asia/Bangkok')

# กำหนดตำแหน่งของโมเดล
model_path = 'model_car(VGG16)\car_model.h5'

#ตำแหน่งที่จะเก็บข้อมูล
path_img = "Snapshot_Data"
path_video = "Video_Data"

# ไว้สำหรับเป็นข้อมูลทั้งหมด เพื่อนำมาเรียงข้อมูลอีกครั้ง
list_path_img = []
list_path_video = []


# เรียกใช้ฟังก์ชันที่เขียนไว้เป็น Class
# -------------------------------------

# เรียกใช้ class ของ Car_Detect
car_detection = Car_Detection()

# เรียกใช้ class ของ Type_Car_Model
type_car_model = Type_Car_Model()

# เรียกใช้ class ของ Type_Car_Img
type_car_img = Type_Car_Img()

# เรียกใช้ class ของ Tesseract
ocr_plate = Tessract_Detect()

# เรียกใช้ class ของ Color
color_car = Color_Detect()

# เรียกใช้ class ของ Color_Flutter
color_flutter = Color_Flutter()

# เรียกใช้ class ของ GDrive
gdrive_img_path = GDrive_Img()


# กระบวนการที่ 1 ของระบบ อ่านวิดีโอ และ ตรวจจับรถ
# -------------------------------------

# # ดัก Error ของารอ่านวิดีโอ
# try:
#   #วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
#   for videos in os.listdir(path_video):
#       #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
#       if (videos.endswith(".mp4")):
              
#               # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
#               full_path_video = path_video + "\\" + str(videos)
              
#               # เพิ่มข้อมูลไฟล์ภาพเข้าไปใน list
#               list_path_video.append(full_path_video)
              
#   for _i ,full_path_video_len in enumerate(natsort.natsorted(list_path_video)):
#         # อ่านไฟล์วิดีโอ โดยใช้ Model ของ MobileNet
#         car_detection.car_detection(full_path_video_len)
    
# # แสดงข้อมูลที่ Error 
# except Exception as e:
#     print("Error: Read Video ")


#  ตั้งค่าเริ่มต้นในการไล่ลำดับของการนับข้อมูล
index = 1

# กระบวนการที่ 2 ของระบบ อ่านตำแหน่งของรูปภาพที่ตรวจจับได้และจัดเก็บใหม่
# -------------------------------------

#วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
for images in os.listdir(path_img):
    # ดัก Error ในการอ่านตำแหน่งของไฟล์
    try:
        #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
        if (images.endswith(".jpg")):
              
              # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
              full_path_img = path_img + "\\" + str(images)
              
              # เพิ่มข้อมูลไฟล์ภาพเข้าไปใน list
              list_path_img.append(full_path_img)
              
    # แสดงข้อมูลที่ Error             
    except Exception as e:
      print('Error: Read Image')
      

# กระบวนการที่ 3 ของระบบ เรียงลำดับของข้อมูลและเข้าสู่กระบวนการอื่นๆ
# -------------------------------------

# ดัก Error ในส่วนของการทำงานระบบหลัก
try:
  # เรียงลำดับข้อมูลให้ถูกต้องแล้วดึงออกมาทีละค่า
  for _i ,full_path_img_len in enumerate(natsort.natsorted(list_path_img)):
        
        
        # ดัก Error ของการตรวจจับประเภทรถ
        try:
            # เริ่มกระบวนการทำงานของ Model Detect Car
            type_model = type_car_model.type_car_model(full_path_img_len, model_path)
            
            # ตรวจสอบประเภทของรถ เพื่อส่ง Path ของรูปภาพไปแสดงผล Frontend
            type_img = type_car_img.type_car_img(type_model)
            
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          print("Error: Cannot load model")
        
        
        # ดัก Error ของการจับ OCR ทะเบียนรถ
        try:
            # เริ่มกระบวนการทำงานของ OCR Detect Plate
            ocr = ocr_plate.tessract_detect(full_path_img_len)
            
            ocr_license_plate = ocr['ป้ายทะเบียน'][0]
            ocr_city_plate = ocr['จังหวัด']
            
            
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          ocr_license_plate = ("Unknown License Plate")
          ocr_city_plate = ("Unknown City Plate")

        
        # ดัก Error ของการจับสีรถ
        try:
            # เริ่มกระบวนการทำงานของ Detect Color
            color = color_car.color_detect(full_path_img_len)
            
            # ตรวจสอบสี เพื่อส่ง ค่าสีของไปแสดงในส่วนของ Frontend
            color_code = color_flutter.color_flutter(color)
                  
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
          os.rename (full_path_img_len,f'{path_img}\{index}_{ocr_license_plate}_{ocr_city_plate}_{type_model}_{color}_{current_time}_{current_date}.jpg')
        
        # แสดงข้อมูลที่ Error  
        except Exception as e:
          print("Error: Rename File")
          
          
        # กระบวนการที่ 5 ของระบบ เปลี่ยื่อไฟล์ให้ถูกต้องตรงกับข้อมูลที่ได้จากการตรวจจับ
        # -------------------------------------
          
        # ดักข้อผิดพลาดอัพโหลดรูปภาพ
        try:
          # เริ่มกระบวนการทำงานของ Upload Image to Google Drive
          img_path = gdrive_img_path.gdrive_img(path_img,index,ocr_license_plate,ocr_city_plate,type_model,color,current_time,current_date)
        
        # แสดงข้อมูลที่ Error  
        except Exception as e:
          print("Error: Google Drive Upload")
          

        # แสดงข้อมูลทั้งหมดเพื่อตรวจสอบ
        
        # แสดงค่าที่ได้ทั้งหมด
        print("index: ",index)
        print("ocr: ",ocr_license_plate)
        print("ocr: ",ocr_city_plate)
        print("type: ",type_model)
        print("type_car_img: ",type_img)
        print("color: ",color)
        print("color_code: ",color_code)
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
                  'car_img_type':type_car_img, # ประเภทรูปภาพ
                  'color': color, # สีรถ
                  'color_code': color_code, # รหัสสีรถ
                  'time': current_time, # เวลา
                  'date': current_date, # วันที่
                  'img': img_path, # ภาพ
                }
        
        # ดักข้อผิดพลาดของ API
        try:
          # ส่งข้อมูลไปยัง API
          post_detel = requests.post(plate_url + '/plates/creates',json=detel_car,headers=headers)
          # แสดงสถานะของ API
          print(post_detel.status_code)
          # แสดงข้อมูลที่ส่ง
          print(post_detel.json())
          
        # แสดงกระบวการที่ผิดพลาด
        except Exception as e:
          print("Error: API")
        
        # เพิ่มค่าของลำดับให้ทำงานได้เป็นลำดับที่ถูกต้อง
        index += 1

except Exception as e:
  print("Error: Main")