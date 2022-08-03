#รวมทุกฟังก์ชัน
# from Object_Detection import *
# from Object_MobileNet import *
from Tesseract import * # ยังไม่สมบูรณ์
from Color import * # ทดสอบผ่านแล้ว
# # from Merge_Image import *
from Type_Car import *
# import cv2

# from Color import *

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

img = cv2.imread('Test_data\y-r46.jpg')
model_path = 'model_car(VGG16)\car_model.h5'
# # blender_5.save("Test_data\image.jpg")

# เรียกใช้ class ของตัวเอง
type_car = Type_Car_Model()
ocr_plate = Tessract_Detect()
color_car = Color_Detect()

# เรียกใช้ฟังก์ชัน
type_car.type_car_model(model_path,img)
ocr_plate.tessract_detect(img)
color_car.color_detect(img)