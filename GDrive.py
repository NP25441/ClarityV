from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import pandas as pd
import natsort, os

class GDrive_Path:
    def __init__(self):
        pass
    
    # ไฟล์ที่ได้จาก Google API Console ในการเข้าถึงข้อมูล
    CLIENT_SECRET_FILE = 'client_secret.json'
    
    # เข้าถึง Google Drive API
    API_NAME = 'drive'
    
    # เวอร์ชั่นของ Google Drive API
    API_VERSION = 'v3'
    
    # สิทธิ์การเข้าถึงข้อมูล
    SCOPES = ['https://www.googleapis.com/auth/drive']
    
    # สร้าง Service สำหรับเข้าถึง Google Drive API
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES) 
    
    def gdrive_img_car(self,path_img,path_index,index,ocr_license_plate,ocr_city_plate,type_model,color,current_time,current_date):
        
        if index <= 9 :
            index_name = f'0{index}'
            
        else:
            index_name = index
            index = index
        
        # กำหนดชื่อไฟล์ที่จะอัพโหลด
        file_name = f'{path_img}\{path_index}\{index}_{ocr_license_plate}_{ocr_city_plate}_{type_model}_{color}_{current_time}_{current_date}.jpg'
        
        # อัพโหลดภาพ
        file_metadata = {
            'name': f'{index_name}', # ชื่อไฟล์ที่จะอัพโหลด
            'parents': ['1GXl9H4o6-u0FEOSq7mAEPqjPyZI2dEQf'] # ตำแหน่งที่อยู่ของไฟล์ที่จะอัพโหลด
        }

        # ระบุชนิดของไฟล์ที่จะอัพโหลด
        media = MediaFileUpload(file_name, mimetype='image/jpg') 

        # สร้างไฟล์
        GDrive_Path.service.files().create( 
            body=file_metadata, 
            media_body=media,
            fields='id'
        ).execute()

        
        index -= 1
        # ดูข้อมูลในไดร์ฟ

        # ตำแหน่งที่อยู่ของไฟล์ที่จะอัพโหลด
        query = f"parents = '1GXl9H4o6-u0FEOSq7mAEPqjPyZI2dEQf'" 

        # ดึงข้อมูลไฟล์ทั้งหมดในไดร์ฟ
        response = GDrive_Path.service.files().list(q=query).execute()

        # ดึงข้อมูลที่เป็นไฟล์
        files = response.get('files')

        # ดึงข้อมูลถัดไป
        nextPageToken = response.get('nextPageToken')

        # แสดงจำนวนและลำดับข้อมูล
        while nextPageToken:
            response = GDrive_Path.service.files().list(q=query, pageToken=nextPageToken).execute()
            files.extend(response.get('files'))
            nextPageToken = response.get('nextPageToken')

        # สร้างการมองเห็นในรูปแบบของ  Data Frame
        df = pd.DataFrame(files)

        # ทำการเรียงลำดับข้องข้อมูล โดยอ้างอิงจากชื่อไฟล์
        drive_data = df.sort_values(by=['name'], axis = 0, ascending=True)

        # เรียงลำดับของตัวเลขใหม่
        drive_data = drive_data.reset_index(drop=True)

        # แสดงข้อมูลแค่เฉพาะ ID ของไฟล์นั้นโดยความคุมลำดับของภาพ
        # print(drive_data['id'][index])
        
        # รวมข้อมูลกับ Path ที่ใช้ในการแสดงรูปภาพ
        img_path_drive_car = 'https://drive.google.com/uc?export=view&id=' + drive_data['id'][index]
        
        # แสดงข้อมูล path ของภาพ
        # print(img_path_drive_car)
        
        # ส่งข้อมูล Path ไปยังฟังก์ชันหลักของระบบ
        return img_path_drive_car
    
    
    # ------------------------------------------------------------------------------
    
    
    def gdrive_img_plate(self,path_plate,index):
            
        if index <= 9 :
            index_name = f'0{index}'
            
        else:
            index_name = index
            index = index
        
        # กำหนดชื่อไฟล์
        file_name = f'{path_plate}\{index}.jpg'
        
        # อัพโหลดภาพ
        file_metadata = {
            'name': f'{index_name}', # ชื่อไฟล์ที่จะอัพโหลด
            'parents': ['1tOwQsc6mHjZJAsKLIZ3oaRj-bMQ7npvH'] # ตำแหน่งที่อยู่ของไฟล์ที่จะอัพโหลด
        }

        # ระบุชนิดของไฟล์ที่จะอัพโหลด
        media = MediaFileUpload(file_name, mimetype='image/jpg') 

        # สร้างไฟล์
        GDrive_Path.service.files().create( 
            body=file_metadata, 
            media_body=media,
            fields='id'
        ).execute()

        
        index -= 1
        # ดูข้อมูลในไดร์ฟ

        # ตำแหน่งที่อยู่ของไฟล์ที่จะอัพโหลด
        query = f"parents = '1tOwQsc6mHjZJAsKLIZ3oaRj-bMQ7npvH'" 

        # ดึงข้อมูลไฟล์ทั้งหมดในไดร์ฟ
        response = GDrive_Path.service.files().list(q=query).execute()

        # ดึงข้อมูลที่เป็นไฟล์
        files = response.get('files')

        # ดึงข้อมูลถัดไป
        nextPageToken = response.get('nextPageToken')

        # แสดงจำนวนและลำดับข้อมูล
        while nextPageToken:
            response = GDrive_Path.service.files().list(q=query, pageToken=nextPageToken).execute()
            files.extend(response.get('files'))
            nextPageToken = response.get('nextPageToken')

        # สร้างการมองเห็นในรูปแบบของ  Data Frame
        df = pd.DataFrame(files)

        # ทำการเรียงลำดับข้องข้อมูล โดยอ้างอิงจากชื่อไฟล์
        drive_data = df.sort_values(by=['name'], axis = 0, ascending=True)

        # เรียงลำดับของตัวเลขใหม่
        drive_data = drive_data.reset_index(drop=True)

        # แสดงข้อมูลแค่เฉพาะ ID ของไฟล์นั้นโดยความคุมลำดับของภาพ
        # print(drive_data['id'][index])
        
        # รวมข้อมูลกับ Path ที่ใช้ในการแสดงรูปภาพ
        img_path_drive_plate = 'https://drive.google.com/uc?export=view&id=' + drive_data['id'][index]
        
        # แสดงข้อมูล path ของภาพ
        # print(img_path_drive_car)
        
        # ส่งข้อมูล Path ไปยังฟังก์ชันหลักของระบบ
        return img_path_drive_plate
    
    
    # ------------------------------------------------------------------------------
    
    
    def gdrive_full_video(self,full_path_video_len,index):
            
        if index <= 9 :
            index_name = f'0{index}'
            
        else:
            index_name = index
            index = index
        
        # กำหนดชื่อไฟล์
        file_name = f'{full_path_video_len}'
        
        # อัพโหลดภาพ
        file_metadata = {
            'name': f'{index_name}', # ชื่อไฟล์ที่จะอัพโหลด
            'parents': ['1aq3LIO8-Uh5AQRet2qP0XzSGwSEY-eRc'] # ตำแหน่งที่อยู่ของไฟล์ที่จะอัพโหลด
        }

        # ระบุชนิดของไฟล์ที่จะอัพโหลด
        media = MediaFileUpload(file_name, mimetype='video/mp4') 

        # สร้างไฟล์
        GDrive_Path.service.files().create( 
            body=file_metadata, 
            media_body=media,
            fields='id'
        ).execute()

        
        index -= 1
        # ดูข้อมูลในไดร์ฟ

        # ตำแหน่งที่อยู่ของไฟล์ที่จะอัพโหลด
        query = f"parents = '1aq3LIO8-Uh5AQRet2qP0XzSGwSEY-eRc'" 

        # ดึงข้อมูลไฟล์ทั้งหมดในไดร์ฟ
        response = GDrive_Path.service.files().list(q=query).execute()

        # ดึงข้อมูลที่เป็นไฟล์
        files = response.get('files')

        # ดึงข้อมูลถัดไป
        nextPageToken = response.get('nextPageToken')

        # แสดงจำนวนและลำดับข้อมูล
        while nextPageToken:
            response = GDrive_Path.service.files().list(q=query, pageToken=nextPageToken).execute()
            files.extend(response.get('files'))
            nextPageToken = response.get('nextPageToken')

        # สร้างการมองเห็นในรูปแบบของ  Data Frame
        df = pd.DataFrame(files)

        # ทำการเรียงลำดับข้องข้อมูล โดยอ้างอิงจากชื่อไฟล์
        drive_data = df.sort_values(by=['name'], axis = 0, ascending=True)

        # เรียงลำดับของตัวเลขใหม่
        drive_data = drive_data.reset_index(drop=True)

        # แสดงข้อมูลแค่เฉพาะ ID ของไฟล์นั้นโดยความคุมลำดับของภาพ
        # print(drive_data['id'][index])
        
        # รวมข้อมูลกับ Path ที่ใช้ในการแสดงรูปภาพ
        video_path_drive = 'https://drive.google.com/uc?export=view&id=' + drive_data['id'][index]
        
        # แสดงข้อมูล path ของภาพ
        # print(img_path_drive_plate)
        
        # ส่งข้อมูล Path ไปยังฟังก์ชันหลักของระบบ
        return video_path_drive