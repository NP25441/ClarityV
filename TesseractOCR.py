#Library ที่เรียกใช้
import pytesseract
import difflib


class Tessract_Detect:
      
      def __init__ (self):
            pass
      
      
      #List ข้อมูลจังหวัด
      City_Ref = ['เชียงราย', 'เชียงใหม่', 'น่าน', 'พะเยา', 'แพร่', 'แม่ฮ่องสอน', 'ลำปาง', 'ลำพูน', 'อุตรดิตถ์', 'กาฬสินธุ์', 'ขอนแก่น', 'ชัยภูมิ', 'นครพนม', 'นครราชสีมา', 'บึงกาฬ', 'บุรีรัมย์', 'มหาสารคาม', 'มุกดาหาร',
            'ยโสธร', 'ร้อยเอ็ด', 'เลย', 'สกลนคร', 'สุรินทร์', 'ศรีสะเกษ', 'หนองคาย', 'หนองบัวลำภู', 'อุดรธานี', 'อุบลราชธานี', 'อำนาจเจริญ', 'กำแพงเพชร', 'ชัยนาท', 'นครนายก', 'นครปฐม', 'นครสวรรค์', 'นนทบุรี',
            'ปทุมธานี', 'พระนครศรีอยุธยา', 'พิจิตร', 'พิษณุโลก', 'เพชรบูรณ์', 'ลพบุรี', 'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สิงห์บุรี', 'สุโขทัย', 'สุพรรณบุรี', 'สระบุรี', 'อ่างทอง', 'อุทัยธานี', 'จันทบุรี', 'ฉะเชิงเทรา',
            'ชลบุรี', 'ตราด', 'ปราจีนบุรี', 'ระยอง', 'สระแก้ว', 'กาญจนบุรี', 'ตาก', 'ประจวบคีรีขันธ์', 'เพชรบุรี', 'ราชบุรี', 'กระบี่', 'ชุมพร', 'ตรัง', 'นครศรีธรรมราช', 'นราธิวาส', 'ปัตตานี', 'พังงา', 'พัทลุง', 'ภูเก็ต', 'ระนอง', 'สตูล',
            'สงขลา', 'สุราษฎร์ธานี', 'ยะลา', 'กรุงเทพมหานคร']

      #List ข้อมูลความถูกต้องของจังหวัด
      city_Ans = []*len(City_Ref)
      

      #List เก็บข้อมูลทั้งหมดมาแสดงผล
      data_show = []*len(City_Ref)


      #เปลี่ยน List เป็น Dict
      def Convert(city_Ans):
            res_dct = {city_Ans[i]: city_Ans[i + 1] for i in range(0, len(city_Ans), 2)}
            return res_dct


      #เรียงลำดับของข้อมูลภายใน List
      def myFunc(e):
            return e['Acc']
      
      
      def tessract_license(self,plate_img):
            
            #อ่านข้อความจากรูปภาพ
            text_license = pytesseract.image_to_string(plate_img , lang='eng+tha_03', config='--psm 11')#ใช้Tesseract-OCR กับ Model ที่สร้างรวมเข้าด้วยกัน

            #ลบการเว้นบรรทัดที่ไม่ต้องการ
            text_license = text_license.split('\n')

            #ลบการเว้นวรรคที่ไม่ต้องการ
            del text_license[1] ,text_license[2]

            #ลบตำแหน่งที่ไม่ต้องการ
            for _i,t1 in enumerate(text_license):
                  text_license = text_license[:_i+1]

                              

            
            ocr_license_plate = text_license
            
            return ocr_license_plate
      
      
      def tessract_city(self,plate_img):
            
            #อ่านข้อความจากรูปภาพ
            text_city = pytesseract.image_to_string(plate_img , lang='tha_03', config='--psm 11')#ใช้Tesseract-OCR กับ Model ที่สร้างรวมเข้าด้วยกัน

            #ลบการเว้นบรรทัดที่ไม่ต้องการ
            text_city = text_city.split('\n')

            #ลบการเว้นวรรคที่ไม่ต้องการ
            del text_city[1] ,text_city[2]

            #ลบตำแหน่งที่ไม่ต้องการ
                  
            for _i,t2 in enumerate(text_city):
                  text_city = t2

            #ลูปที่ใช้เปรียบเทียบความถูกต้องของข้อความที่ได้จากรูปภาพ
            for _i ,city in enumerate (Tessract_Detect.City_Ref):
                  seq = difflib.SequenceMatcher(None,text_city,city)
                  Accuracy = seq.ratio()*100
                  if Accuracy >= 30.00:
                        Tessract_Detect.city_Ans.append({'จังหวัด':city,'Acc':Accuracy})
                              

            Tessract_Detect.city_Ans.sort(key=Tessract_Detect.myFunc, reverse=True)
            
            print(Tessract_Detect.city_Ans)
            #แสดงข้อมูลที่ได้จากรูปภาพ
            ocr_city_plate = Tessract_Detect.city_Ans[0]

            
            return ocr_city_plate
