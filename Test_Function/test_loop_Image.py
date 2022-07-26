import cv2
from PIL import Image
from PIL import Image, ImageGrab
import os


images_per_class = 80
fixed_size       = (620, 480)
path       = "Test_Loop_Tessract"

# train_labels = os.listdir(path)
# for training_name in train_labels:
#     
#         current_label = training_name
#         for x in range(1,images_per_class+1):
#         # get the image file name
#             full_path = path + "\\" + str(x) + ".jpg"
#             # read the image and resize it to a fixed-size
#             img = cv2.imread(full_path)
#             img = cv2.resize(img, fixed_size)
#             print(full_path)
#     except Exception as e:
#         print(str(e))
        # D:\Develop\Senior_Project\ClarityV\plate_loop_test\g-bk0.jpg
        
for images in os.listdir(path):
    # check if the image end swith png or jpg or jpeg
    if (images.endswith(".jpg")):
        full_path = path + "\\" + str(images)
        img = cv2.imread(full_path)
        img = cv2.resize(img, (620,480) ) #ปรับขนาดรูปภาพ
        # display
        print(img)