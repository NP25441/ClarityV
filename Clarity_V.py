#รวมทุกฟังก์ชันที่เรียกใช้
import os ,sys ,requests ,pytz ,natsort ,json
from Model_Plate import * # ทดสอบผ่านแล้ว
from Car_Detect import * # ทดสอบผ่านแล้ว
from Color import * # ทดสอบผ่านแล้ว
from EasyOcr import * # ทดสอบผ่านแล้ว
from Type_Car_Model import * # ทดสอบผ่านแล้ว
from GDrive import * # ทดสอบผ่านแล้ว
from Name_Random import * # ทดสอบผ่านแล้ว 
from datetime import datetime,date


# กำหนดค่าเริ่มต้น
# -----------------------------------------------------------------------------------------------------------------------------------------------------


# ตำแหน่ง API
plate_url = "https://d741-2001-fb1-10b-d49b-4d97-efa2-d0b-b8ac.ap.ngrok.io"

# ตั้งค่า Timezone
tz = pytz.timezone('Asia/Bangkok')

# กำหนดตำแหน่งของโมเดล
model_path = 'model_car(VGG16)\car_model.h5' # ประเภทรถ

#ตำแหน่งที่จะเก็บข้อมูล
path_img = "Snapshot_Car"
path_plate = "Snapshot_Plate"
path_video = "Video_Data"

# ไว้สำหรับเป็นข้อมูลทั้งหมด เพื่อนำมาเรียงข้อมูลอีกครั้ง
list_path_img = []
list_path_video = []
list_path_drive_video =[]


# เรียกใช้ฟังก์ชันที่เขียนไว้เป็น Class
# -----------------------------------------------------------------------------------------------------------------------------------------------------


#  เรียกใช้งาน Class ของ Model_Plate
model_plate = Model_Plate()

# เรียกใช้งาน Class ของ Name_Random
name_random = Name_Random()

# เรียกใช้ class ของ Car_Detect
car_detection = Car_Detection()

# เรียกใช้ class ของ Type_Car_Model
type_car_model = Type_Car_Model()

# เรียกใช้ class ของ EasyOcr
easyocr_plate = EasyOcr_Plate()

# เรียกใช้ class ของ Color
color_car = Color_Detect()

# เรียกใช้ class ของ GDrive
gdrive_path = GDrive_Path()


# กระบวนการที่ 1 ของระบบ อ่านวิดีโอ และ ตรวจจับรถ
# -----------------------------------------------------------------------------------------------------------------------------------------------------


# ดัก Error ของารอ่านวิดีโอ
try:
  #  ตั้งค่าเริ่มต้นในการไล่ลำดับของการนับข้อมูล
  index = 1

  sec_time = []

  # วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
  for videos in os.listdir(path_video):
      #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
      if (videos.endswith(".mp4")):
              
              # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
              full_path_video = path_video + "\\" + str(videos)
              
              # เพิ่มข้อมูลไฟล์ภาพเข้าไปใน list
              list_path_video.append(full_path_video)


  # เรียงชื่อไฟล์ให้เป็นไปตามลำดับ
  for _i ,full_path_video_len in enumerate(natsort.natsorted(list_path_video)):
        # อ่านไฟล์วิดีโอ โดยใช้ Model ของ MobileNet

        time_video = car_detection.car_detection(index, full_path_video_len)
        sec_time.append(time_video)
        
        # ดักข้อผิดพลาดของการ Upload ไฟล์
        try :
          # Upload ไฟล์วิดีโอ ไปยัง Google Drive
          video_path_drive = gdrive_path.gdrive_full_video(full_path_video_len,index)

          list_path_drive_video.append(video_path_drive)
          
          print(list_path_drive_video)
        
        # แสดงข้อผิดพลาดของการ Upload ไฟล์
        except Exception as e:
          print("Error: upload video to drive")
        
        # เพิ่มค่าของ index
        index += 1


# แสดงข้อมูลที่ Error 
except Exception as e:
    print("Error: Video not found")


# กระบวนการที่ 2 ของระบบ อ่านตำแหน่งของรูปภาพที่ตรวจจับได้และจัดเก็บใหม่
# -----------------------------------------------------------------------------------------------------------------------------------------------------


# จัดการวินาทีที่ตรวจจับได้ของวิดีโอ
try:
  # ค่าเริ่มต้นของลำดับ
  sec_time_over_len = []
  
  for _i ,sec_time_list in enumerate(sec_time):
        for _i ,sec_time_list_len in enumerate(sec_time_list):
              sec_time_over_len.append(sec_time_list_len)

# แสดงข้อมูลที่ Error 
except Exception as e:
    print("Error: Len Sec Video")


try:
  #  ตั้งค่าเริ่มต้นในการไล่ลำดับของการนับข้อมูล
  index = 1
  sec_time_index = 0

  # อ่านชื่อ directory ของรูปภาพที่ตรวจจับได้
  dir_list = os.listdir(path_img)

  # จัดลำดับของชื่อ directory ใหม่
  for _i ,full_path_split_video_len in enumerate(natsort.natsorted(dir_list)):

    #วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
    for images in os.listdir(f"{path_img}\{full_path_split_video_len}"):

      # ดัก Error ในการอ่านตำแหน่งของไฟล์
      try:
          #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
          if (images.endswith(".jpg")):
                
                # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
                full_path_img = path_img + "\\" + full_path_split_video_len + "\\" + str(images)
                
                # เพิ่มข้อมูลไฟล์ภาพเข้าไปใน list
                list_path_img.append(full_path_img)
                
      # แสดงข้อมูลที่ Error             
      except Exception as e:
        print('Error: Read Image')


    # กระบวนการที่ 3 ของระบบ เรียงลำดับของข้อมูลและเข้าสู่กระบวนการอื่นๆ
    # -----------------------------------------------------------------------------------------------------------------------------------------------------


    # ดัก Error ในส่วนของการทำงานระบบหลัก
    try:
      # เรียงลำดับข้อมูลให้ถูกต้องแล้วดึงออกมาทีละค่า
      for _i ,full_path_img_len in enumerate(natsort.natsorted(list_path_img)):
          
        # แยกชื่อไฟล์ Video 
        path_index = full_path_img_len.split("\\")
        
        # เลือกตำแหน่งที่เป็นชื่อของ Directory
        path_index = path_index[1]
        
        # แปลงค่าของ Directory ให้เป็นตัวเลขและกำหนดให้เแป็นลำดับของ List
        if path_index != 0:
              video_index = int(path_index)
              video_index = video_index - 1
        
        
        # ดัก Error ของการตรวจจับประเภทรถ
        try:
            # เริ่มกระบวนการทำงานของ Model Detect Car
            type_model = type_car_model.type_car_model(full_path_img_len, model_path)
            
            # ตรวจสอบประเภทของรถ เพื่อส่ง Path ของรูปภาพไปแสดงผล Frontend
            type_car_img = type_car_model.type_car_img(type_model)
        
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          print("Error: Cannot load model")
        
        
        # ดัก Error ของการตรวจจับประเภทรถ
        try:
            # เริ่มกระบวนการทำงานของ Model Detect Car
            plate_img = model_plate.model_plate(index, full_path_img_len)
            
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          print("Error: plate_img")
          
          # กำหนดค่ากรณีที่ไม่พบป้ายทะเบียน
          plate_img = 'Plate Not Found'
        
        
        # ดัก Error ของการจับ OCR ทะเบียนรถ
        try:
            # เริ่มกระบวนการทำงานของ OCR Detect Plate
            ocr_license_plate = easyocr_plate.ocr_license_plate(plate_img)
        
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          ocr_license_plate = ("Unknown License Plate")
        
        
        # ดัก Error ของการจับ OCR จังหวัด
        try:
          # เริ่มกระบวนการทำงานของ OCR Detect Plate
          ocr_city_plate = easyocr_plate.ocr_city_plate(plate_img)
          
          ocr_city_plate = ocr_city_plate['จังหวัด']
        
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          ocr_city_plate = ("Unknown City Plate")


        # ดัก Error ของการจับสีรถ
        try:
            # เริ่มกระบวนการทำงานของ Detect Color
            color = color_car.color_detect(full_path_img_len)
            
            # ตรวจสอบสี เพื่อส่ง ค่าสีของไปแสดงในส่วนของ Frontend
            color_code = color_car.color_flutter(color)
        
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          print("Error: Detect Color")
        
        
        # ดัก Error ของการตั้งค่าเวลา และ วันที่
        try:
          # ตั้งค่าเวลา
          # กำหนดโซนเวลาและเวลาปัจจุบัน
          time_tz = datetime.now(tz)
          # กำหนดรูปแบบเวลา
          current_time = time_tz.strftime("%H:%M")
          
          # ตั้งค่าวันที่
          # ตั้งค่าวันที่ปัจจุบัน
          date_tz = date.today()
          # กำหนดรูปแบบวันที่
          current_date = date_tz.strftime("%d/%m/%Y")
          
        # แสดงข้อมูลที่ Error 
        except Exception as e:
          print("Error: Detect Color")
        
        
        # ตรวจสอบว่ามีข้อมูลที่ถูกต้องหรือไม่
        if plate_img == 'Plate Not Found' :
              # คืนค่าข้อมูล
              index = index
              # แสดงข้อมูลที่ตรวจสอบผิดพลาด
              print("Plate Not Found")
              
        else:
              # ทำงานต่อหากไม่พบข้อผิดพลาดในระบบ
              
              # กระบวนการที่ 4 ของระบบ เปลี่ยื่อไฟล์ให้ถูกต้องตรงกับข้อมูลที่ได้จากการตรวจจับ
              # -----------------------------------------------------------------------------------------------------------------------------------------------------
              
              # ดักข้อผิดพลาดของการเปลี่ยนชื่อไฟล์
              try:
                # เปลี่ยนชื่อไฟล์
                os.rename (full_path_img_len,f'{path_img}\{path_index}\{index}_{ocr_license_plate}_{ocr_city_plate}_{type_model}_{color}.jpg')
              
              # แสดงข้อมูลที่ Error  
              except Exception as e:
                print("Error: Rename File")


              # กระบวนการที่ 5 ของระบบ เปลี่ยื่อไฟล์ให้ถูกต้องตรงกับข้อมูลที่ได้จากการตรวจจับ
              # -----------------------------------------------------------------------------------------------------------------------------------------------------

              # ดักข้อผิดพลาดอัพโหลดรูปภาพ
              try:
                # เริ่มกระบวนการทำงานของ Upload Image to Google Drive
                img_path_car = gdrive_path.gdrive_img_car(path_img,path_index,index,ocr_license_plate,ocr_city_plate,type_model,color)
              
                img_path_plate = gdrive_path.gdrive_img_plate(path_plate,index)
              
              # แสดงข้อมูลที่ Error  
              except Exception as e:
                print("Error: Google Drive Upload")
                
              
              try:
                name = name_random.name_random(index)
                
              except Exception as e:
                print("Error: Name Random")


              # แสดงข้อมูลทั้งหมดเพื่อตรวจสอบ
              
              try:
                # แสดงค่าที่ได้ทั้งหมด
                print("index: ", index)
                print("ocr_license: ", ocr_license_plate)
                print("ocr_city: ", ocr_city_plate)
                print('name: ', name)
                print("type: ", type_model)
                print("type_car_img: ", type_car_img)
                print("color: ", color)
                print("color_code: ", color_code)
                print("time: ", current_time)
                print("date: ", current_date)
                print ("path_img_car: ", img_path_car)
                print ("path_img_plate: ", img_path_plate)
                print("video: ", f'{list_path_drive_video[video_index]}?t={sec_time_over_len[sec_time_index]}s')
                
              except Exception as e:
                print("Error: Show Data")
              
              
              # กระบวนการที่ 6 ของระบบ รวมข้อมูลทั้งหมดและส่งข้อมูลไป API
              # -----------------------------------------------------------------------------------------------------------------------------------------------------
              
              
              # ดักข้อผิดพลาดของ API
              try:
                # Header ของไฟล์ 
                headers = {'Accept': 'application/json', # รับค่าเป็น json
                            'content-type': 'application/json', # ส่งค่าเป็น json
                            'Access-Control_Allow_Origin': '*'} # ส่งค่าไปที่ทุกๆที่
                
                # เรียงลำดับของข้อมูลที่จะส่งไปยัง API
                detel_car = { 'id': f'{index}', # รหัสรถ
                          'license_plate': f'{ocr_license_plate}', # ทะเบียนรถ
                          'name': f'{name}', # ชื่อเจ้าของรถ
                          'city': f'{ocr_city_plate}', # จังหวัด
                          'vehicle': f'{type_model}', # ประเภทรถ
                          'car_img_type': f'{type_car_img}', # ประเภทรูปภาพ
                          'color': f'{color}', # สีรถ
                          'color_code': f'{color_code}', # รหัสสีรถ
                          'time': f'{current_time}', # เวลา
                          'date': f'{current_date}', # วันที่
                          'img_car': f'{img_path_car}', # ภาพรถ
                          'img_plate': f'{img_path_plate}', # ภาพป้ายทะเบียน
                          'video': f'{list_path_drive_video[video_index]}?t={sec_time_over_len[sec_time_index]}s', # วิดีโอ
                        }
                
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
        sec_time_index += 1


    # แสดงข้อมูลที่ทำงานผิดพลาด
    except Exception as e:
      print("Error: Status Process")

# แสดงข้อมูลที่ทำงานผิดพลาด
except Exception as e:
  print("Error: Main")