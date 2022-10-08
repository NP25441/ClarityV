import numpy as np 
import cv2


class Color_Detect:
    def __init__ (self):
        pass
    
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    def color_detect(self,full_path):
        image = cv2.imread(full_path)
        image = cv2.resize(image, (1000, 700))
        rate_area = 1000
        
        Color_Detect = []
        Color_Num = {}

        SHV_Frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

        # สีแดง --
        red_lower = np.array([160,0,0], np.uint8) 
        red_upper = np.array([179,255,255], np.uint8) 
        red_mask = cv2.inRange(SHV_Frame, red_lower, red_upper)
        # สีน้ำเงิน --
        blue_lower = np.array([75,0,0], np.uint8) 
        blue_upper = np.array([100,255,255], np.uint8) 
        blue_mask = cv2.inRange(SHV_Frame, blue_lower, blue_upper) 
        # สีเหลือง --
        yellow_lower = np.array([22,0,0], np.uint8)
        yellow_upper = np.array([38,255,255], np.uint8)
        yellow_mask = cv2.inRange(SHV_Frame, yellow_lower, yellow_upper)
        # สีขาว
        white_lower = np.array([255,0,227], np.uint8)
        white_upper = np.array([0,0,255], np.uint8)
        white_mask = cv2.inRange(SHV_Frame, white_lower, white_upper)
        # สีดำ       
        black_lower = np.array([0,0,0], np.uint8)
        black_upper = np.array([0,255,33], np.uint8)
        black_mask = cv2.inRange(SHV_Frame, black_lower, black_upper)
        # สีม่วง
        violet_lower= np.array([130, 52, 72], np.uint8)
        violet_upper = np.array([160,255,255], np.uint8)
        violet_mask = cv2.inRange(SHV_Frame, violet_lower, violet_upper)
        # สีเขียว --
        green_lower = np.array([38,0,0], np.uint8) 
        green_upper = np.array([75,255,255], np.uint8) 
        green_mask = cv2.inRange(SHV_Frame, green_lower, green_upper) 
        # สีส้ม --
        orange_lower = np.array([0,52,176], np.uint8)
        orange_upper = np.array([22,255,255], np.uint8)
        orange_mask = cv2.inRange(SHV_Frame, orange_lower, orange_upper)
        # สีน้ำตาล
        brown_lower = np.array([24,255,255], np.uint8)
        brown_upper = np.array([35,255,151], np.uint8)
        brown_mask = cv2.inRange(SHV_Frame, brown_lower, brown_upper)
        # สีชมพู
        pink_lower = np.array([111, 52, 72], np.uint8)
        pink_upper = np.array([149, 255, 255], np.uint8)
        pink_mask = cv2.inRange(SHV_Frame, pink_lower, pink_upper)
        # สีเทา
        gray_lower = np.array([0,0,226], np.uint8)
        gray_upper = np.array([255,255,107], np.uint8)
        gray_mask = cv2.inRange(SHV_Frame, gray_lower, gray_upper)
        # สีฟ้า
        light_blue_lower = np.array([100, 52, 72], np.uint8) 
        light_blue_upper = np.array([130, 255, 255], np.uint8)
        light_blue_mask = cv2.inRange(SHV_Frame, light_blue_lower, light_blue_upper)


        # Morphological Transform, Dilation 
        # for each color and bitwise_and operator 
        # between SHV_Frame and mask determines 
        # to detect only that particular color 
        kernal = np.ones((5, 5), "uint8") 


        # แปลงค่าสำหรับสีแดง
        red_mask = cv2.dilate(red_mask, kernal) 
        # res_red = cv2.bitwise_and(SHV_Frame, image, mask = red_mask)
        # Creating contour to track red color 
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area):
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
                # cv2.putText(image, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
                # print("Red Colour")
                Color_Detect.append("สีแดง")


        # แปลงค่าสำหรับสีส้ม
        orange_mask = cv2.dilate(orange_mask, kernal) 
        # res_orange = cv2.bitwise_and(SHV_Frame, image, mask = orange_mask)
        # Creating contour to track Orange Colour
        contours, hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > rate_area):
                x, y, w, h = cv2.boundingRect(contour)
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 128, 0), 2)
                
                # cv2.putText(image, "Orange Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 128, 0))
                # print("Orange Colour")
                Color_Detect.append("สีส้ม")


        # แปลงค่าสำหรับสีเหลือง
        yellow_mask = cv2.dilate(yellow_mask, kernal) 
        # res_yellow = cv2.bitwise_and(SHV_Frame, image, mask = yellow_mask) 
        # Creating contour to track Yellow Colour
        contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (49,255,255), 2) 
                
                # cv2.putText(image, "Yellow Colour", (x, y), 1.0, (49,255,255))
                # print("Yellow Colour")
                Color_Detect.append("สีเหลือง")


        # แปลงค่าสำหรับสีเขียว
        green_mask = cv2.dilate(green_mask, kernal) 
        # res_green = cv2.bitwise_and(SHV_Frame, image, mask = green_mask) 
        # Creating contour to track Green Colour
        contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
                
                # cv2.putText(image, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
                # print("Green Colour")
                Color_Detect.append("สีเขียว")


        # แปลงค่าสำหรับสีฟ้า
        blue_mask = cv2.dilate(blue_mask, kernal) 
        # res_blue = cv2.bitwise_and(SHV_Frame, image, mask = blue_mask)
        # Creating contour to track Blue Colour
        contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) 
                
                # cv2.putText(image, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
                # print("Blue Colors")
                Color_Detect.append("สีน้ำเงิน")


        # แปลงค่าสำหรับสีม่วง
        violet_mask = cv2.dilate(violet_mask, kernal) 
        # res_violet = cv2.bitwise_and(SHV_Frame, image, mask = violet_mask)
        # Creating contour to track Violet Colour
        contours, hierarchy = cv2.findContours(violet_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (204,102,255), 2) 
                
                # cv2.putText(image, "Violet Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (204,102,255))
                # print("Violet Colour")
                Color_Detect.append("สีม่วง")


        # แปลงค่าสำหรับสีดำ
        black_mask = cv2.dilate(black_mask, kernal) 
        # res_black = cv2.bitwise_and(SHV_Frame, image, mask = black_mask)
        # Creating contour to track Black Colour
        contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
                
                # cv2.putText(image, "Black Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Black Colour")
                Color_Detect.append("สีดำ")


        # แปลงค่าสำหรับสีขาว
        white_mask = cv2.dilate(white_mask, kernal) 
        # res_white = cv2.bitwise_and(SHV_Frame, image, mask = white_mask)
        # Creating contour to track White Colour
        contours, hierarchy = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2) 
                
                # cv2.putText(image, "White Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
                # print("White Colour")
                Color_Detect.append("สีขาว")


        # แปลงค่าสำหรับสีเทา
        gray_mask = cv2.dilate(gray_mask, kernal) 
        # res_gray = cv2.bitwise_and(SHV_Frame, image, mask = gray_mask)
        # Creating contour to track Gray Colour
        contours, hierarchy = cv2.findContours(gray_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
                
                # cv2.putText(image, "Gray Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Gray Colour")
                Color_Detect.append("สีเทา")


        # แปลงค่าสำหรับสีชมพู
        pink_mask = cv2.dilate(pink_mask, kernal) 
        # res_pink = cv2.bitwise_and(SHV_Frame, image, mask = pink_mask)
        # Creating contour to track Pink Colour
        contours, hierarchy = cv2.findContours(pink_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
                
                # cv2.putText(image, "Pink Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Pink Colour")
                Color_Detect.append("สีชมพู")


        # แปลงค่าสำหรับสีน้ำตาล
        brown_mask = cv2.dilate(brown_mask, kernal) 
        # res_brown = cv2.bitwise_and(SHV_Frame, image, mask = brown_mask)
        # Creating contour to track Brown Colour
        contours, hierarchy = cv2.findContours(brown_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
                
                # cv2.putText(image, "Brown Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Brown Colour")
                Color_Detect.append("สีน้ำตาล")


        # แปลงค่าสำหรับสีฟ้า
        light_blue_mask = cv2.dilate(light_blue_mask, kernal) 
        # res_light_blue = cv2.bitwise_and(SHV_Frame, image, mask = light_blue_mask)
        # Creating contour to track Light Blue Colour
        contours, hierarchy = cv2.findContours(light_blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                SHV_Frame = cv2.rectangle(image, (x, y), (x + w, y + h), (149, 255, 255), 2) 
                
                # cv2.putText(image, "Light Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (149, 255, 255))
                # print("Light Blue Colour")
                Color_Detect.append("สีฟ้า")


        for x in Color_Detect:
            if x in Color_Num:
                Color_Num[x] += 1
            else:
                Color_Num[x] = 1
                


        def myFunc(e):
            return e[1]

        Color_Car = [(k, v) for k, v in Color_Num.items()]

        Color_Car.sort(key=myFunc, reverse=True)
        color = Color_Car[0]
        color = color[0]
        # print("Detect Color is: ",color)
        
        return color
    
    
    # -----------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    def color_flutter(self, color):
        
        # ตรวจสอบสี เพื่อส่ง ค่าสีของไปแสดงในส่วนของ Frontend
        if color == 'สีแดง':
              color_code = 'Color(0xFFFD0110)'
        elif color == 'สีส้ม':
              color_code = 'Color(0xFFFE8A00)'
        elif color == 'สีเหลือง':
              color_code = 'Color(0xFFFEFB00)'
        elif color == 'สีเขียว':
              color_code = 'Color(0xFF08810E)'
        elif color == 'สีน้ำเงิน':
              color_code = 'Color(0xFF0012FF)'
        elif color == 'สีม่วง':
              color_code = 'Color(0xFF6F36A9)'
        elif color == 'สีดำ':
              color_code = 'Colors.black'
        elif color == 'สีขาว':
              color_code = 'Color.fromARGB(255, 255, 255, 255)'
        elif color == 'สีเทา':
              color_code = 'Color(0xFF8E8E8E)'
        elif color == 'สีชมพู':
              color_code = 'Color(0xFFFF6790)'
        elif color == 'สีน้ำตาล':
              color_code = 'Color(0xFF901901)'
        elif color == 'สีฟ้า':
              color_code = 'Color(0xFF00D0FD)'
        
        # print('Color Code : ',color_code)
        
        return color_code