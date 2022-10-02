class Color_Flutter(object):
    def __init__ (self): 
        pass
    
    
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
        
        print('Color Code : ',color_code)
        
        return color_code