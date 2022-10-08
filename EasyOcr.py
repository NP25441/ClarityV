import os, difflib, easyocr, cv2
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import numpy as np

class EasyOcr_Plate:
    def __init__ (self):
        pass
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------------
    

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
    
    
    def ocr_license_plate(self,plate_img):

        reader = easyocr.Reader(['th'])
        ocr_result_license = reader.readtext(plate_img)
        
        ocr_license_plate = ocr_result_license[0][1]
        
        return ocr_license_plate
    
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    def ocr_city_plate(self,plate_img):

        reader = easyocr.Reader(['th'])
        ocr_result_city = reader.readtext(plate_img)
        
        ocr_city_plate = ocr_result_city[1][1]
        
        # print('test', ocr_city_plate)
        
        #ลูปที่ใช้เปรียบเทียบความถูกต้องของข้อความที่ได้จากรูปภาพ
        for _i ,city in enumerate (EasyOcr_Plate.City_Ref):
                seq = difflib.SequenceMatcher(None,ocr_result_city[1][1],city)
                Accuracy = seq.ratio()*100
                if Accuracy >= 30.00:
                    EasyOcr_Plate.city_Ans.append({'จังหวัด':city,'Acc':Accuracy})
                            

        EasyOcr_Plate.city_Ans.sort(key=EasyOcr_Plate.myFunc, reverse=True)
        
        # print(EasyOcr_Plate.city_Ans)
    
        ocr_city_plate = EasyOcr_Plate.city_Ans[0]
        
        return ocr_city_plate