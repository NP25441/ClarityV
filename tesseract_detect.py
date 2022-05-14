import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
from PIL import Image, ImageGrab

img = cv2.imread('y-r47.jpg') #นำเข้ารูปภาพ
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









#Read the number plate
text = pytesseract.image_to_string(Cropped , lang='tha_01+eng+tha_02+tha_00+eng_00+tha', config='--psm 11')
print("Detected Number is:",text)

cv2.imshow("Image", Cropped)
cv2.waitKey(0)
