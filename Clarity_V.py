#รวมทุกฟังก์ชัน
# from Object_Detection import *
# from Object_MobileNet import *
from Car_Detect import *
from Color import *
from Tesseract import * # ทดสอบผ่านแล้ว
# # from Merge_Image import *
from Type_Car import *

#ตั้งค่าตัวแปร
# image1 = Image.open("Test_data\car (1).jpg")
# image2 = Image.open("Test_data\car (2).jpg")
# image3 = Image.open("Test_data\car (3).jpg")
# image4 = Image.open("Test_data\car (4).jpg")
# image5 = Image.open("Test_data\car (5).jpg")
# image6 = Image.open("Test_data\car (6).jpg")

# blender_1 = Image.blend(image1,image2,0.2)
# blender_2 = Image.blend(image3,blender_1,0.2)
# blender_3 = Image.blend(image4,blender_2,0.2)
# blender_4 = Image.blend(image5,blender_3,0.2)
# blender_5 = Image.blend(image6,blender_4,0.2)

# # blender_5.save("Test_data\image.jpg")

cap = cv2.VideoCapture('Test_data\Video-3.mp4')
# img = cv2.imread('Test_data\y-r46.jpg')
model_path = 'model_car(VGG16)\car_model.h5'

#ตำแหน่งของข้อมูลในเครื่อง
path       = "Snapshot_Data\Line_1"

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

#วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
for images in os.listdir(path):
    # ดัก Error แล้วเด้งออกจากโปรแกรม
    try:
        #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
        if (images.endswith(".jpg")):
                full_path = path + "\\" + str(images)
                
                # ดัก Error แล้วเด้งออกจากโปรแกรม
                try:
                    #รัน Model Detect Car
                    type_car.type_car_model(model_path,full_path)
                # แสดงค่าที่ Error
                except Exception as e:
                  print("Error: Cannot load model")
                
                # ดัก Error แล้วเด้งออกจากโปรแกรม
                try:
                    #รัน OCR Detect Plate
                    ocr_plate.tessract_detect(full_path)
                # แสดงค่าที่ Error
                except Exception as e:
                  print("Error: Detect Plate")
                
                # ดัก Error แล้วเด้งออกจากโปรแกรม  
                try:
                    # รัน Detect Color
                    color_car.color_detect(full_path)
                # แสดงค่าที่ Error 
                except Exception as e:
                  print("Error: Detect Color")
    
    # แสดงค่าที่ Error            
    except Exception as e:
                  print(str(e))