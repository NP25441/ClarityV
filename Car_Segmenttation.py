import numpy, cv2, os
from turtle import width
from PIL import Image

class Car_Segmanttation:
    
    def __init__ (self):
        pass
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    def car_segment(self, index, full_path_img_len):
        
        # โหลด Model ที่เราจะใช้
        net = cv2.dnn.readNetFromTensorflow("model_segment(R-CNN)\\frozen_inference_graph.pb","model_segment(R-CNN)\mask_rcnn_inception_v2_coco_2018_01_28.pbtxt")
        
        # โหลดรูปภาพที่จะทำการตรวจจับ
        img = cv2.imread("Test_data\car (9).png")
        
        # กำหนดขนาดของรูปภาพ
        height, width, channels = img.shape

        # กำหนดให้เป็น Array
        black_img = numpy.zeros(img.shape[:3], dtype="uint8")

        # จัดการข้อมูลของ Model
        blob = cv2.dnn.blobFromImage(img, swapRB=True)
        net.setInput(blob)
        boxes, masks = net.forward(["detection_out_final", "detection_masks"])
        detection_count = boxes.shape[2]

        # ทำการหาวัตถุภายในภาพ
        for i in range(detection_count):
            
            # กำหนดการสร้างกรอบ
            box = boxes[0, 0, i]
            
            # กำหนด Class ของวัตถุ
            class_id = box[1]
            
            # กำหนดความน่าจะเป็นของวัตถุ
            score = box[2]
            if score < 0.5:
                continue

            # สร้างตำแหน่งกรอบของวัตถุ
            x = int(box[3] * width)
            y = int(box[4] * height)
            x2 = int(box[5] * width)
            y2 = int(box[6] * height)
            
            # สร้าง Mask ของวัตถุ
            mask = masks[i, int(class_id)]
            
            # กำหนดขนาดของ Mask
            mask = cv2.resize(mask, (width, height))
            
            # กำหนดความละเอียดของ Mask และ กำหนดค่า Threshold
            channels, mask = cv2.threshold(mask, 0.7, 255, cv2.THRESH_BINARY)
            
            # กำหนดค่าของสี
            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

        # นำข้อมูลที่ได้มาทำการ Overlay กับรูปภาพ   
        test = img / mask
        test = test + img

        # save รูปภาพ
        cv2.imwrite("test.png", test)
    
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------------


    def transpatent_segmenttation(self, index, full_path_img_len):
        
        # เปิดรูปภาพ
        img = Image.open(full_path_img_len)
        
        # แปลงสีของรูปภาพ
        img = img.convert("RGBA")
        
        # กำหนดค่าของสีที่จะทำการทำให้เป็นโปร่งใส
        datas = img.getdata()
        
        # เพิ่มข้อมูลใหม่
        newData = []
        
        # หาค่าของสีที่จะทำให้เป็นโปร่งใส
        for item in datas:
            
            # หาค่าสีดำ
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                # ทำให้เป็นโปร่งใส
                newData.append((255, 255, 255, 0))
                
            else:
                # คือนำค่าสีเดิมมาใช้
                newData.append(item)
                
        # เพิ่มข้อมูลใหม่
        img.putdata(newData)
        
        # save รูปภาพ
        img.save(f"Car_Segment\\seg_{index}.png", "PNG")
        
        # กำหนดตำแหน่งของรูปภาพเดิม
        path_seg = os.path.join(path_seg)
        
        # ลบรูปภาพเดิม
        os.remove(path_seg)