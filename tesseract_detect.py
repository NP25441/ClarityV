#Library ที่เรียกใช้
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
from PIL import Image, ImageGrab
import difflib


#List ข้อมูลจังหวัด
City_Ref = ['เชียงราย', 'เชียงใหม่', 'น่าน', 'พะเยา', 'แพร่', 'แม่ฮ่องสอน', 'ลำปาง', 'ลำพูน', 'อุตรดิตถ์', 'กาฬสินธุ์', 'ขอนแก่น', 'ชัยภูมิ', 'นครพนม', 'นครราชสีมา', 'บึงกาฬ', 'บุรีรัมย์', 'มหาสารคาม', 'มุกดาหาร',
        'ยโสธร', 'ร้อยเอ็ด', 'เลย', 'สกลนคร', 'สุรินทร์', 'ศรีสะเกษ', 'หนองคาย', 'หนองบัวลำภู', 'อุดรธานี', 'อุบลราชธานี', 'อำนาจเจริญ', 'กำแพงเพชร', 'ชัยนาท', 'นครนายก', 'นครปฐม', 'นครสวรรค์', 'นนทบุรี',
        'ปทุมธานี', 'พระนครศรีอยุธยา', 'พิจิตร', 'พิษณุโลก', 'เพชรบูรณ์', 'ลพบุรี', 'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สิงห์บุรี', 'สุโขทัย', 'สุพรรณบุรี', 'สระบุรี', 'อ่างทอง', 'อุทัยธานี', 'จันทบุรี', 'ฉะเชิงเทรา',
        'ชลบุรี', 'ตราด', 'ปราจีนบุรี', 'ระยอง', 'สระแก้ว', 'กาญจนบุรี', 'ตาก', 'ประจวบคีรีขันธ์', 'เพชรบุรี', 'ราชบุรี', 'กระบี่', 'ชุมพร', 'ตรัง', 'นครศรีธรรมราช', 'นราธิวาส', 'ปัตตานี', 'พังงา', 'พัทลุง', 'ภูเก็ต', 'ระนอง', 'สตูล',
        'สงขลา', 'สุราษฎร์ธานี', 'ยะลา', 'กรุงเทพมหานคร']

#List ข้อมูลความถูกต้องของจังหวัด
city_Ans = []

#List เก็บข้อมูลทั้งหมดมาแสดงผล
data_show = []


#เปลี่ยน List เป็น Dict
def Convert(city_Ans):
      res_dct = {city_Ans[i]: city_Ans[i + 1] for i in range(0, len(city_Ans), 2)}
      return res_dct


#เรียงลำดับของข้อมูลภายใน List
def myFunc(e):
      return e['Acc']

#ตำแหน่งของข้อมูลในเครื่อง
path       = "D:\Develop\Senior_Project\ClarityV\plate_loop_test"


#กระบวนการทำงานของ CV2
img = cv2.imread('plate_loop_test\y-r165.jpg') #นำเข้ารูปภาพ
img = cv2.resize(img, (620,480) ) #ปรับขนาดรูปภาพ
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #แปลงรูปภาพเป็นเฉพาะสีขาว-ดำ
gray = cv2.bilateralFilter(gray, 11, 17, 17) #ทำให้รูปภาพเบลอเพื่อแยกสีให้ชัดเจนขึ้น
edged = cv2.Canny(gray, 30, 200) #สักเอาขอบของรูปภาพผ่าน Filter

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

plate = []
# loop over our contours
for c in cnts:
 # approximate the contour
 peri = cv2.arcLength(c, True)
 approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
 # if our approximated contour has four points, then
 # we can assume that we have found our screen
 if len(approx) == 4:
  screenCnt = approx
  plate.append(screenCnt)

 
if screenCnt is None:
 detected = 0
 print ("No contour detected")
else:
 cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

# Masking the part other than the number plate
mask = np.zeros(gray.shape,np.uint8)
print(mask)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)

# Now crop
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]


#print(pytesseract.image_to_boxes(Cropped))

h_Cropped, w_Cropped = Cropped.shape
boxes = pytesseract.image_to_boxes(Cropped)

for b in boxes.splitlines():
      b = b.split(' ')
      z,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
      # print (z,y,w,h)
      cv2.rectangle(Cropped,(z,h_Cropped-y),(w,h_Cropped-h),(255,255,0),2)


#อ่านข้อความจากรูปภาพ
text_1 = pytesseract.image_to_string(Cropped , lang='eng+tha_03', config='--psm 11')#ใช้Tesseract-OCR กับ Model ที่สร้างรวมเข้าด้วยกัน
text_2 = pytesseract.image_to_string(Cropped , lang='tha_03', config='--psm 11')#ใช้Tesseract-OCR กับ Model ที่สร้างรวมเข้าด้วยกัน

#ลบการเว้นบรรทัดที่ไม่ต้องการ
text_1 = text_1.split('\n')
text_2 = text_2.split('\n')

#ลบการเว้นวรรคที่ไม่ต้องการ
del text_1[1] ,text_1[2]
del text_2[1] ,text_2[2]

#ลบตำแหน่งที่ไม่ต้องการ
for _i,t1 in enumerate(text_1):
      text_1 = text_1[:_i+1]
      
for _i,t2 in enumerate(text_2):
      #text_l1 = text_1[_i]
      text_2 = t2

#ลูปที่ใช้เปรียบเทียบความถูกต้องของข้อความที่ได้จากรูปภาพ
for _i ,city in enumerate (City_Ref):
      seq = difflib.SequenceMatcher(None,text_2,city)
      Accuracy = seq.ratio()*100
      if Accuracy >= 30.00:
            city_Ans.append({'ป้ายทะเบียน':text_1,'จังหวัด':city,'Acc':Accuracy})
            

city_Ans.sort(key=myFunc, reverse=True)
data_show.append(city_Ans[0])


#แสดงข้อมูลที่ได้จากรูปภาพ
print("Detected City is: ",data_show)



#แสดงภาพที่ได้จากการคำนวณ
#cv2.imshow("Image", Cropped)#แสดงรูปภาพที่ได้จากการทำงาน
#cv2.waitKey(0)#รอการกดปุ่มเพื่อคืนค่า
