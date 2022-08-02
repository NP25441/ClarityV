import cv2
import numpy as np

#our target area (the black background)
# dst = np.zeros((100,100),dtype=np.int)
src1 = cv2.imread("Test_data\car (4).jpg")
src1 = cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
src2 = cv2.imread("Test_data\car (5).jpg")
src2 = cv2.cvtColor(src2,cv2.COLOR_BGR2RGB)
src1[1400:,600:] = 1 #fake of first translated image (row/col 50-end)
src2[:2000,:3700] = 1 #fake of second translated image (row/col 0-70)

overlap = src1+src2 #sum of both *element-wise*

cv2.imwrite('Test_data\car (1).jpg', src1*255) #opencv likes it's grey images span from 0-255
cv2.imwrite('Test_data\car (2).jpg', src2*255) #...
cv2.imwrite('Test_data\car (3).jpg', overlap*255) #here vals 0-2, *127 gives (almost) 255 again

np.where(overlap==2) #gives you a mask with all pixels that have value 2