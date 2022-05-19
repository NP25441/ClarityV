import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
from PIL import Image, ImageGrab
import pythainlp.util
from pythainlp.tokenize.multi_cut import find_all_segment, mmcut, segment
from pythainlp.corpus.common import thai_words
from pythainlp.util import Trie
from pythainlp import word_tokenize

city = ['เชียงราย', 'เชียงใหม่', 'น่าน', 'พะเยา', 'แพร่', 'แม่ฮ่องสอน', 'ลำปาง', 'ลำพูน', 'อุตรดิตถ์', 'กาฬสินธุ์', 'ขอนแก่น', 'ชัยภูมิ', 'นครพนม', 'นครราชสีมา', 'บึงกาฬ', 'บุรีรัมย์', 'มหาสารคาม', 'มุกดาหาร',
        'ยโสธร', 'ร้อยเอ็ด', 'เลย', 'สกลนคร', 'สุรินทร์', 'ศรีสะเกษ', 'หนองคาย', 'หนองบัวลำภู', 'อุดรธานี', 'อุบลราชธานี', 'อำนาจเจริญ', 'กำแพงเพชร', 'ชัยนาท', 'นครนายก', 'นครปฐม', 'นครสวรรค์', 'นนทบุรี',
        'ปทุมธานี', 'พระนครศรีอยุธยา', 'พิจิตร', 'พิษณุโลก', 'เพชรบูรณ์', 'ลพบุรี', 'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สิงห์บุรี', 'สุโขทัย', 'สุพรรณบุรี', 'สระบุรี', 'อ่างทอง', 'อุทัยธานี', 'จันทบุรี', 'ฉะเชิงเทรา',
        'ชลบุรี', 'ตราด', 'ปราจีนบุรี', 'ระยอง', 'สระแก้ว', 'กาญจนบุรี', 'ตาก', 'ประจวบคีรีขันธ์', 'เพชรบุรี', 'ราชบุรี', 'กระบี่', 'ชุมพร', 'ตรัง', 'นครศรีธรรมราช', 'นราธิวาส', 'ปัตตานี', 'พังงา', 'พัทลุง', 'ภูเก็ต', 'ระนอง', 'สตูล',
        'สงขลา', 'สุราษฎร์ธานี', 'ยะลา', 'กรุงเทพมหานคร']

img = cv2.imread('y-r46.jpg') #นำเข้ารูปภาพ
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
      print (z,y,w,h)
      cv2.rectangle(Cropped,(z,h_Cropped-y),(w,h_Cropped-h),(255,255,0),2)


#อ่านข้อความจากรูปภาพ
text = pytesseract.image_to_string(Cropped , lang='eng_00+tha+tha_00+tha_01+tha_02+eng', config='--psm 11')#ใช้Tesseract-OCR กับ Model ที่สร้างนวมเข้าด้วยกัน
print("Detected Number is: ",text.replace(" ",""))#แสดงผลลัพธ์ที่ได้จากการอ่านข้อความ
word_tokenize(text, keep_whitespace=False)
print(find_all_segment(text))


cv2.imshow("Image", Cropped)#แสดงรูปภาพที่ได้จากการทำงาน
cv2.waitKey(0)#รอการกดปุ่มเพื่อคืนค่า
