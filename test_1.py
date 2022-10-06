import numpy, cv2
from turtle import width


# Loading Mask RCNN
net = cv2.dnn.readNetFromTensorflow("model_segment(R-CNN)\\frozen_inference_graph.pb","model_segment(R-CNN)\mask_rcnn_inception_v2_coco_2018_01_28.pbtxt")

img = cv2.imread("Test_data\car (9).png")
height, width, channels = img.shape

black_img = numpy.zeros(img.shape[:3], dtype="uint8")


# Detect objects
blob = cv2.dnn.blobFromImage(img, swapRB=True)
net.setInput(blob)

boxes, masks = net.forward(["detection_out_final", "detection_masks"])
detection_count = boxes.shape[2]

for i in range(detection_count):
    box = boxes[0, 0, i]
    class_id = box[1]
    score = box[2]
    if score < 0.5:
        continue

    # Get box Coordinates
    x = int(box[3] * width)
    y = int(box[4] * height)
    x2 = int(box[5] * width)
    y2 = int(box[6] * height)
    
    mask = masks[i, int(class_id)]
    mask = cv2.resize(mask, (width, height))
    channels, mask = cv2.threshold(mask, 0.7, 255, cv2.THRESH_BINARY)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    
test = img / mask


# print(test.shape)

# datas = test.getdata()

# newData = []

# for item in datas:
#     if item[0] == 0 and item[1] == 0 and item[2] == 0:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("test_1.png", "PNG")
# print("Successful")

# masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask Applied to Image", test)
cv2.imwrite("test.png", test) 
cv2.waitKey(0)
