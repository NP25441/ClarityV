import cv2
import os
import natsort

path = "Video-Data"
path_video = []

#วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
for images in os.listdir(path):
    #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
    if (images.endswith(".mp4")):
            
            # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
            full_path = path + "\\" + str(images)
            
            # เพิ่มข้อมูลไฟล์ภาพเข้าไปใน list
            path_video.append(full_path)

for _i ,full_path in enumerate(natsort.natsorted(path_video)):
        
    cap = cv2.VideoCapture(full_path)
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

