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

        # d = []
        # v = []

        # Start a while loop 
        # ret, image = image.read()
        kernel = np.ones((7,7),np.uint8) 

        Frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 


        # สีแดง --
        red_lower = np.array([0, 50, 100], np.uint8) 
        red_upper = np.array([14, 255, 255], np.uint8) 
        red_mask = cv2.inRange(Frame, red_lower, red_upper)
        mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = red_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area):
                x, y, w, h = cv2.boundingRect(contour) 
                red_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
                cv2.putText(image, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
                # print("Red Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีแดง")
        
        # สีส้ม --
        orange_lower = np.array([15, 50,200], np.uint8)
        orange_upper = np.array([20,255,255], np.uint8)
        orange_mask = cv2.inRange(Frame, orange_lower, orange_upper)
        mask = cv2.morphologyEx(orange_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(orange_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(orange_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area =  orange_mask
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > rate_area):
                x, y, w, h = cv2.boundingRect(contour)
                orange_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 128, 0), 2)
                
                cv2.putText(image, "Orange Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 128, 0))
                # print("Orange Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีส้ม")
                
        # สีเหลือง --
        yellow_lower = np.array([25, 50, 107], np.uint8)
        yellow_upper = np.array([35,255,255], np.uint8)
        yellow_mask = cv2.inRange(Frame, yellow_lower, yellow_upper)
        mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = yellow_mask
        for pic, contours in enumerate(contours): 
            area = cv2.contourArea(contours) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contours) 
                yellow_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (49,255,255), 2) 
                
                cv2.putText(image, "Yellow Colour", (x, y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (49,255,255))
                # print("Yellow Colour")
        # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีเหลือง")

        # สีเขียว --
        green_lower = np.array([40, 50, 107], np.uint8) 
        green_upper = np.array([70, 255, 255], np.uint8) 
        green_mask = cv2.inRange(Frame, green_lower, green_upper)
        mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel) 
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3) 
        area = green_mask
        for pic, contours in enumerate(contours):
            area = cv2.contourArea(contours) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contours) 
                green_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
                
                cv2.putText(image, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
                # print("Green Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีเขียว")

        # สีฟ้า
        light_blue_lower = np.array([85, 150, 107], np.uint8) 
        light_blue_upper = np.array([100, 255, 255], np.uint8)
        light_blue_mask = cv2.inRange(Frame, light_blue_lower, light_blue_upper)
        mask = cv2.morphologyEx(light_blue_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(light_blue_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(light_blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = light_blue_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                light_blue_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (149, 255, 255), 2) 
                
                cv2.putText(image, "Light Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (149, 255, 255))
                # print("Light Blue Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีฟ้า")

        # สีน้ำเงิน --
        blue_lower = np.array([110,  50, 80], np.uint8) 
        blue_upper = np.array([130, 255, 255], np.uint8)   
        blue_mask = cv2.inRange(Frame, blue_lower, blue_upper) 
        mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = blue_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                blue_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) 
                
                cv2.putText(image, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
                # print("Blue Colors")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีน้ำเงิน")

        # สีม่วง
        violet_lower= np.array([135, 50, 107], np.uint8)
        violet_upper = np.array([140,255,255], np.uint8)
        violet_mask = cv2.inRange(Frame, violet_lower, violet_upper)
        mask = cv2.morphologyEx(violet_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(violet_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(violet_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = violet_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                violet_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (204,102,255), 2) 
                
                cv2.putText(image, "Violet Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (204,102,255))
                # print("Violet Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีม่วง")
        
        # สีชมพู
        pink_lower = np.array([150,50, 0], np.uint8)
        pink_upper = np.array([160,255,255], np.uint8)
        pink_mask = cv2.inRange(Frame, pink_lower, pink_upper)
        mask = cv2.morphologyEx(pink_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(pink_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(pink_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = pink_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                pink_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2)
                
                
                cv2.putText(image, "Pink Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Pink Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีชมพู")

        # สีขาว
        white_lower = np.array([0,0,209], np.uint8)
        white_upper = np.array([0,0,255], np.uint8)
        white_mask = cv2.inRange(Frame, white_lower, white_upper)
        mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = white_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                white_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2) 
                
                cv2.putText(image, "White Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
                # print("White Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีขาว")

        # สีดำ       
        black_lower = np.array([0,0,0], np.uint8)
        black_upper = np.array([0,255,33], np.uint8)
        black_mask = cv2.inRange(Frame, black_lower, black_upper)
        mask = cv2.morphologyEx(black_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = black_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                black_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
                
                cv2.putText(image, "Black Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Black Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีดำ")

        # สีเทา
        gray_lower = np.array([255,0,0], np.uint8)
        gray_upper = np.array([0,0,171], np.uint8)
        gray_mask = cv2.inRange(Frame, gray_lower, gray_upper)
        mask = cv2.morphologyEx(gray_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(gray_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(gray_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        output = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
        area = gray_mask 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                gray_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
                
                cv2.putText(image, "Gray Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Gray Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีเทา")
        
        # สีน้ำตาล
        brown_lower = np.array([12,218,145], np.uint8)
        brown_upper = np.array([26,255,159], np.uint8)
        brown_mask = cv2.inRange(Frame, brown_lower, brown_upper)
        mask = cv2.morphologyEx(brown_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(brown_mask, cv2.MORPH_OPEN, kernel)
        segmented_img = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(brown_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
        area = brown_mask
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > rate_area): 
                x, y, w, h = cv2.boundingRect(contour) 
                brown_mask = cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,0), 2) 
                
                cv2.putText(image, "Brown Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))
                # print("Brown Colour")
                # # print(x, y, w, h)
                area = (x + w)*( y + h)
                # print(area)
                Color_Detect.append("สีน้ำตาล")


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