import os

#ตำแหน่งที่จะเก็บข้อมูล
path       = "Snapshot-Data"

index = []
ocr = []
type = []
color = []

#วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
for images in os.listdir(path):
    # ดัก Error แล้วเด้งออกจากโปรแกรม
    try:
        #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
        if (images.endswith(".jpg")):
              # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
                full_path = path + "\\" + str(images)
                
                name_img = full_path.split("_")
                print(name_img)
                
                
                
                count_index = name_img[0].split("\\")
                count_index.remove("Snapshot-Data")
                index.append(count_index)
                
                ocr.append(name_img[1])
                
                type.append(name_img[2])
                
                name_color = name_img[3].split(".")
                name_color.remove("jpg")
                color.append(name_color)
                
                # print(name_color)
                
                
                
                # y = x.split("_")
                # print(y)
    
    # แสดงค่าที่ Error            
    except Exception as e:
                  print("str(e)")

print(index)                  
print(ocr)
print(type)
print(color)

                  
