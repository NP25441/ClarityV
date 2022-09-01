# ClarityV

# Read Video
 - สามารถรับไฟล์วีดีโอเข้ามาและทำการเล่นไฟล์นั้น

# Detect Plate_OCR
 - เปลี่ยนจากการรับข้อมูลในรูปแบบของวีดีโอเป็นภาพ
 - ทำให้ระบบสามารถตรวจจับตัวอักษรบนภาพได้ด้วยการทำงานของ Tesseract OCR
 - Train Tesseract ใหม่ด้วยควบรวมระบบของ ตัวต้นแบบเข้าใช้งานกับที่ได้มใาจากการ Train เพื่อเพิ่มประสิทธิภาพของผลลัพธ์

# Text_V.1
 - เพิ่มการทำงานของระบบ PyThai NLP
 - เพิ่มข้อมูลของจังหวัดเข้าไปเพื่อให้ให้มีการเปรียบเทียบกับข้อมูลที่ถูกต้อง

# Edit Text
 - ปรับแก้ผลลัพธ์ที่ได้จากการทำงานของ Tesseract เพราะมีส่วนที่ไม่ต้องการเยอะเกินไป
 - ปรับรูปแบบของคำให้มีความเหมาะสมและถูกหลักไวยกรณ์

# SequenceMatcher
 - ทำให้ระบบทำการเปรียบเทียบตัวอักษรการข้อมูลของจังหวัดที่ถูกต้อง
 - โดยการเรียนใช้งาน SequenceMatcher มาใช้ในการหาสัดส่วนของความถูกต้องโดยให้เป็นคะนนเพื่อใช้ในการเรียงลำดับความน่าเชื่อถือ

# Voting Ensembles
 - นำผลลัพธ์ที่ได้จากการทำงานของ SequenceMatcher มาเก็บลงในรูปแบบของ Dict ที่ซ้อนอยู่ภายใน List เพื่อให้มีการดึงค่าออกมาใช้ได้
 - เรียงลำดับของข้อมูลโดยอ้างอิงจากการทำงานของ SequenceMatcher ที่ให้คำแนนความเหมือนมากที่สุดมาเป็นลำดับแรก
 - หลังจากมีการ Sort แล้วให้มีการดึงข้อมูลออกมาโดยดึงข้อมูล 10 อันดับแรกออกมาแสดงผล

# Detect Vehicle
 - ทำระบบตรวจจับวัตถุเคลื่อนไหว
 - ทำให้มีการแสดงผล 2 ส่วนคือ 
   - การแสดงผลปกติ 
   - การแสดงผลเฉพาะสิ่งที่เคลื่อนไหว
 - สร้างเส้นขึ้นมา 2 เส้นเพื่อตรวจจับวัตุที่ผ่านเส้นจะทำการนับจำนวนวัตถุที่ผ่านเส้น
 - ทำให้ทั้ง 2 เส้นมีการกระพริบเปลี่ยนสีได้ตอนที่วัตถุผ่าน
 - เพิ่มไฟล์วิดีโอของสถานที่จริง

# Snapshot 
 - เพิ่มการจับภาพหน้าจอ
 - จับภาพหน้าจอโดยการลบเส้นที่ใช้ในการตรวจจับออกแต่เก็บกรอบที่ใช้สำหรับตรวจจับไว้
 - ทดสอบการแสดงผล 1080p และ 3840p

# Loop_V_1
 - เพิ่ม Path ของข้อมูลที่จะใช้ในการดึงข้อมูล
 - ปรับชุดข้อมูลให้เป็นชุดเพื่อใช้ในการส่งข้อมูลออกให้กับ API
 - ปรับรูปแบบของการแสดงข้อมูลเพียง 1 ค่าเพื่อให้นำมาแสดงผลได้

# Loop_V_2
 - ใช้งานลูปให้มีการเรียกไฟล์ใน Path ที่กำหนดไว้ทั้งหมด
 - ทำการอ่านค่าที่ละภาพและปรับขนาดให้เท่ากัน
 - ใช้ความสามารถของ OCR ดึงตัวอักษรออกมาใส่ลงในชุดข้อมูลที่กำหนดไว้
 - ปรับชุดข้อมูลเพื่อลดความซ้ำซ้อน
 - ดึงค่าที่ดีที่สุดมาทำการแสดงผลเพียง 1 ค่า
 - จัดชุดข้อมูลให้สามารถส่งให้กับ API ได้

# Model_V_1
 - เพิ่มความสามารถการอ่าน Model (ยังไม่สมบูรณ์)
 - สามารถเข้าถึง Model
 - ปรับแก้และทดสอบค่าของการ Input และทดสอบผลของ Tessract
 - ประแก้ชุดภาษาของ Tessract 
 - เพิ่มข้อมูล Class ของประเภทที่จะทำการใส่ Segment (ยังไม่สมบูรณ์)

# Model_V_2
 - ไม่ได้นำตัวของ Model ที่ทำใน Model_V_1 มาใช้
 - ใช้ Model ของ Mobile Net SSD มาทำการตรวจจับวัตถุ
 - สร้างกรอบ ชื่อ ของการตรวจจับโดย Mobile Net SSD
 - สร้างผลลัพธ์การแสดงผลของฟังก์ชัน และจะนำไปใช้งานต่อในการทำ SnapShot
 - ** สร้าง Model การตรวจจับใหม่ขึ้นมาแต่อยู่ใน Google Colab **

# Test_Flask (Test)
 - ทดลองสร้าง Flask ขึ้นมาเพื่อที่จะทำการทดลองแสดงค่าบนการทำงานของ Dart / Flutter
 
# Merge Image (ไม่ได้ใช้งาน)
 - รวมภาพทั้งหมด 6 ภาพให้เป็นภาพเดียวเพื่อให้ภาพมีความชัดมากที่สุด
 - ส่งภาพออกมาทดสอบ(FPS ที่ได้จากกล้องที่ถ่ายมาไม่มากพอทำให้ผลลัพธ์ไม่ดีอย่างที่คิด)
 
# Image Convert Video (Test)
 - นำโมเดลที่สร้างใน Google Colab ที่มาจากหัวข้อ Model_V_2 มาทดสอบ
 - ผลลัพธ์ที่ได้จะเป็น การทำกรอบและระบุชนิดที่ได้ชัดเจนอยู่แล้ว
 - ทำการส่งออกมาเป็นภาพตาม FPS
 - นำภาพที่ได้ทั้งหมดกลับมาต่อเป็น Video อีกครั้ง
 
# Color_Detect
 - ตรวจจับสีภายในภาพนิ่ง
 - ทำการสร้างกรอบล้อมรอบสีนั้น
 - สร้างกล้องข้อความบอกข้อมูลเกี่ยวกับสีนั้นๆที่ตรวจจับได้
 - ทำการส่งค่าของสีออกมาโดยตรวจจับจำนวนของสีที่ตรวจจับได้
 - นำค่าที่ตรวจจับได้ที่มาเรียงลำดับที่มากที่สุด
 - แสดงข้อมูลของลำดับที่ตรวจจับได้ที่มาที่สุดออกมาเพียงค่าเดียว
 
# Combile_V_1
 - สร้างหน้าของการใช้แบบรวมขึ้นมา
 - รวมการทำงานของ Color Detect กับ Tessract เข้าด้วยกัน
 - สามารถทำงานได้ในเงื่อนไขของข้อมูลที่ตามที่กำหนดเท่านั้น
 - Tesract ยังไม่ปัญหาในการทำ OCR กับภาพรวมของการทำงาน

# Overlap (ไม่ได้ใช้งาน)
 - ลองสร้างการทำงานที่มีภาพตัดกัน
 - นำภาพที่ตัดกันมาใช้งาน

# Type_Car_Model
 - นำเข้า Car Model VGG16 ในรูปแบบ H5
 - ทำการส่งข้อมูลไปยังใน Model แล้วทำการ Predict ผล
 - นำผลมาเทียบกับข้อมูลแล้วส่งข้อมูลออกมาตามประเภทที่กำหนด
 - รวมชุดคำสั่งกับระบบการทำงานหลักของระบบ

# Combile_V_2
 - ปรับแก้ Path ของตำแหน่ง Model VGG16
 - เปิดการใช้งาน Tessract 
 - ทดสอบทำงานเบื้องต้น

# Snapshot
 - เพิ่มการจับภาพหน้าจอตอนที่ Point ของวัตถุสัมผัสที่เส้น
 - ลบเส้นของภาพที่ตรวจจับ แต่เก็บกรอบของวัตถุไว้

# Crop_Image
 - หลังจาก Snapshot แล้วให้ทำการ Crop โดยอิงจากรอบของวัตถุที่ตรวจับได้

# Combile_V_3
 - รวมชุดคำสั่งของ Snapshot กับ Crop_Image เข้ากับชุดการทำงานหลัก
 - ปรับการทำงานให้มีความต่อเนื่องของการทำงานในระบบ

# Flask_V_1 
 - เพิ่งฟังก์ชันของ Flask ขึ้นมา
 - ปรับการทำงานจากแบบเดิมที่มีการทำงานที่ซับซ้อนของไฟล์ให้เป็นไฟล์เดียว
 - สร้างเส้นทางการเชื่อมข้อมูลระหว่างหน้า และแสดงข้อมูล
 - ทดสอบการทำงานเบื้องต้นของ Flask

# Combile_V_4
 - เพิ่มฟังก์ชัน ในการดัก Error และสามารถทำงานในฟังก์ชันต่อไปได้โดยไม่เด้งออก
 - ปรับแก้ตัวแปรให้มีการสร้าง Path ที่เชื่อมโยง
 - เพิ่มความสามารถในการรันแบบการสร้างลูปที่ต่อเนื่องจาก Path ครบทุกตำแหน่ง

# Rename_Data
 - นำภาพที่ได้จากการ Snapshot มาทำการหาคุณสมบัติต่างๆ ป้ายทะเบียน สี ประเภท
 - ทำคุณสมบัติทั้งหมดมาทำเป็นชื่อไฟล์ เชื่อส่งข้อมูลให้ Data Base โดยจะถือว่าได้ผลลัพธ์ที่สามารถใช้แล้ว

# Split_Name
 - เพิ่มฟังก์ชันในการอ่านชื่อไฟล์จาก path ของเครื่อง
 - คัดแยกคุณสมบัติที่ใส่ไว้ในชื่อไฟล์ออกมาตามประเภทที่จัดกลุ่มไว้
 - จัดชุดข้อมูลสำหรับเตรียมส่งเข้า Database ผ่าน API
 - ปรับปรุงตำแหน่งของแกน แกน X และ Y ในการทำ Crop Image
 - เพิ่มไฟล์การเชื่อมต่อกับ MongoDB ผ่าน API



# ส่วนที่ต้องปรับแก้และยังไม่ได้ทำ
 - ปรับการ Crop_Image (เสร็จแล้ว)
 - ปรับลำดับการทำงานของผลลัพธ์
 - ปรับชุดข้อมูลให้มีความสอดคล่องกับ Data Base
 - ปรับประสิทธิภาพของชุดการทำงาน
 - ปรับประสิทธิภาพของ Tessract
