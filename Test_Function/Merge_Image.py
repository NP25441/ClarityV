from PIL import Image
import PIL

image1 = Image.open("Test_data\car (1).jpg")
image2 = Image.open("Test_data\car (2).jpg")
image3 = Image.open("Test_data\car (3).jpg")
image4 = Image.open("Test_data\car (4).jpg")
image5 = Image.open("Test_data\car (5).jpg")
image6 = Image.open("Test_data\car (6).jpg")

blender_1 = Image.blend(image1,image2,0.2)
blender_2 = Image.blend(image3,blender_1,0.2)
blender_3 = Image.blend(image4,blender_2,0.2)
blender_4 = Image.blend(image5,blender_3,0.2)
blender_5 = Image.blend(image6,blender_4,0.2)

img = blender_5
#Image.blend(blender_1,blender_1,00)

img.save("Test_data\image.jpg")
