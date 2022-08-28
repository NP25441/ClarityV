#import libraryที่จำเป็น
import numpy as np 
import cv2

# #รายชื่อหมวดหมู่ทั้งหมด เรียงตามลำดับ
# CLASSES = ["BACKGROUND", "AEROPLANE", "BICYCLE", "BIRD", "BOAT",
# 	"BOTTLE", "BUS", "CAR", "CAT", "CHAIR", "COW", "DININGTABLE",
# 	"DOG", "HORSE", "MOTORBIKE", "PERSON", "POTTEDPLANT", "SHEEP",
# 	"SOFA", "TRAIN", "TVMONITOR"]

# #ตำแหน่งของเส้น
# pos_line_1 = 450
# pos_line_2 = 650

# #ฟังก์ชันบอกจุดทีแดงที่เป็นใจกลางของกรอบ detect	
# def coordinate_red_dot(x, y, w, h):
#     x1 = int(w / 3)
#     y1 = int(h / 3)
#     cx = x + x1
#     cy = y + y1
#     return cx,cy

# #กำหนดอัตราการผิดพลาดที่น่าเชื่อถือ
# offset= 10

# #นับจำนวนรูปที่ snapshot ได้
# count_1 = 0
# count_2 = 0

# #สีตัวกรอบที่วาดrandomใหม่ทุกครั้ง
# COLORS = np.random.uniform(0,100, size=(len(CLASSES), 3))

# #โหลดmodelจากแฟ้ม
# net = cv2.dnn.readNetFromCaffe("model_car(MobileNet)\MobileNetSSD.prototxt","model_car(MobileNet)\MobileNetSSD.caffemodel")



#เลือกวิดีโอ/เปิดกล้อง
# cap = cv2.VideoCapture('Test_data\Video-3.mp4')

class Car_Detection:
    
    def __init__(self):
        pass
    
    #รายชื่อหมวดหมู่ทั้งหมด เรียงตามลำดับ
    CLASSES = ["BACKGROUND", "AEROPLANE", "BICYCLE", "BIRD", "BOAT",
	"BOTTLE", "BUS", "CAR", "CAT", "CHAIR", "COW", "DININGTABLE",
	"DOG", "HORSE", "MOTORBIKE", "PERSON", "POTTEDPLANT", "SHEEP",
	"SOFA", "TRAIN", "TVMONITOR"]
    #โหลดmodelจากแฟ้ม
    net = cv2.dnn.readNetFromCaffe("model_car(MobileNet)\MobileNetSSD.prototxt","model_car(MobileNet)\MobileNetSSD.caffemodel")
    
    #ตำแหน่งของเส้น
    pos_line_1 = 450
    # pos_line_2 = 650
    
    #ฟังก์ชันบอกจุดทีแดงที่เป็นใจกลางของกรอบ detect
    def coordinate_red_dot(x, y, w, h):
        x1 = int(w / 3)
        y1 = int(h / 3)
        cx = x + x1
        cy = y + y1
        return cx,cy
    
    #ใช้เก็บค่าของจุด X,Y
    detect_1 = []
    # detect_2 = []
    
    #นับจำนวนของรถที่ตรวจจับได้ในระบบ
    detect_line_1 = 0
    # detect_line_2 = 0
    
    #กำหนดอัตราการผิดพลาดที่น่าเชื่อถือ
    offset= 10
    
    #นับจำนวนรูปที่ snapshot ได้
    count_1 = 0
    # count_2 = 0
    
    #สีตัวกรอบที่วาดrandomใหม่ทุกครั้ง
    COLORS = np.random.uniform(0,100, size=(len(CLASSES), 3))
    
    frameTime = 1 # time of each frame in ms, you can add logic to change this value.
    
    def car_detection(self, cap):
        while True:
            #เริ่มอ่านในแต่ละเฟรม
            ret, frame = cap.read()
            if ret:
                h,w = frame.shape[:2]
                #ทำpreprocessing
                blob = cv2.dnn.blobFromImage(frame, 0.007843, (300,300), 300)
                Car_Detection.net.setInput(blob)
                #feedเข้าmodelพร้อมได้ผลลัพธ์ทั้งหมดเก็บมาในตัวแปร detections
                detections = Car_Detection.net.forward()
                
                for i in np.arange(0, detections.shape[1]):
                    percent = detections[0,0,i,2]
                    #สร้างเส้นสำหรับตรวจจับรถ เส้นที่ 1
                    cv2.line(frame, (300, Car_Detection.pos_line_1), (1800, Car_Detection.pos_line_1), (255,127,0), 2)
                    # # สร้างเส้นสำหรับตรวจจับรถ เส้นที่ 2
                    # cv2.line(frame, (300, Car_Detection.pos_line_2), (1800, Car_Detection.pos_line_2), (255,127,0), 2)
                    #กรองเอาเฉพาะค่าpercentที่สูงกว่า0.5 เพิ่มลดได้ตามต้องการ
                    if percent > 0.6:
                        class_index = int(detections[0,0,i,1])
                        box = detections[0,0,i,3:7]*np.array([w,h,w,h])
                        (startX, startY, endX, endY) = box.astype("int")
                        coordinate = Car_Detection.coordinate_red_dot(startX, startY, endX, endY)
                        #ส่วนตกแต่งสามารถลองแก้กันได้ วาดกรอบและชื่อ
                        label = "{} [{:.2f}%]".format(Car_Detection.CLASSES[class_index], percent*100)
                        cv2.rectangle(frame, (startX, startY), (endX, endY), Car_Detection.COLORS[class_index], 2)
                        cv2.rectangle(frame, (startX-1, startY-30), (endX+1, startY), Car_Detection.COLORS[class_index], cv2.FILLED)
                        y = startY - 15 if startY-15>15 else startY+15
                        cv2.putText(frame, label, (startX+20, y+5), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255,255,255), 1)
                        Car_Detection.detect_1.append(coordinate)
                        # Car_Detection.detect_2.append(coordinate)
                        cv2.circle(frame, coordinate, 4, (0, 0,255), -1)
                        
                        #เส้นตรวจจับที่ 1
                        for (x,y) in Car_Detection.detect_1:
                            if y<(Car_Detection.pos_line_1 + Car_Detection.offset) and y>(Car_Detection.pos_line_1 - Car_Detection.offset):
                                Car_Detection.detect_line_1 += 1
                                cv2.line(frame, (300, Car_Detection.pos_line_1), (1800, Car_Detection.pos_line_1), (0,127,255), 2)
                                Car_Detection.detect_1.remove((x,y))
                                print("Detected_1 : " + str(Car_Detection.detect_line_1))
                                ret, frame = cap.read()
                                frame = cv2.rectangle(frame, (startX, startY), (endX, endY), Car_Detection.COLORS[class_index], 2)
                                frame = frame[y:startX+200 + startY+100, x:endX + endY]
                                cv2.imwrite("Snapshot_Data\image_%d.jpg" % Car_Detection.count_1, frame)    
                                print('Saved image ', Car_Detection.count_1)
                                Car_Detection.count_1 += 1
                                #print(detect_1)
                                
                        # #เส้นตรวจจับที่ 2
                        # for (x,y) in Car_Detection.detect_2:
                        #     if y<(Car_Detection.pos_line_2 + Car_Detection.offset) and y>(Car_Detection.pos_line_2 - Car_Detection.offset):
                        #         Car_Detection.detect_line_2 += 1
                        #         cv2.line(frame, (300, Car_Detection.pos_line_2), (1800, Car_Detection.pos_line_2), (0,127,255), 2)  
                        #         Car_Detection.detect_2.remove((x,y))
                        #         print("Detected_2 : "+str(Car_Detection.detect_line_2))
                        #         ret, frame = cap.read()
                        #         frame = cv2.rectangle(frame, (startX, startY), (endX, endY), Car_Detection.COLORS[class_index], 2)
                        #         frame = frame[y:(startX, startY), x:(endX, endY)]
                        #         cv2.imwrite("Snapshot_Data\Line_2\image_2_%d.jpg" % Car_Detection.count_2, frame)    
                        #         print('Saved image ', Car_Detection.count_2)
                        #         Car_Detection.count_2 += 1
                        #         #print(detect_2)
                              
            cv2.imshow("Frame", frame)
            if cv2.waitKey(Car_Detection.frameTime) & 0xFF == ord('q'):
                break
        
        # #หลังเลิกใช้แล้วเคลียร์memoryและปิดกล้อง
        # cap.release()
        # cv2.destroyAllWindows()
        
		
