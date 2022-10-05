import os
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import cv2 
import numpy as np
import easyocr
import difflib
import natsort

path_img = "Snapshot_Data"

list_path_img = []

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

#วนลูปในไฟล์ของตำแหน่งที่ตั้งไหล์
for images in os.listdir(path_img):
    # ดัก Error ในการอ่านตำแหน่งของไฟล์
    try:
        #เช็คว่ามีภาพที่เป็นไฟล์นามสกุล .jpg หรือไม่
        if (images.endswith(".jpg")):
              
              # ปรับตำแหน่งของไฟล์ภาพให้ถูกต้อง
              full_path_img = path_img + "\\" + str(images)
              
              # เพิ่มข้อมูลไฟล์ภาพเข้าไปใน list
              list_path_img.append(full_path_img)
              
    # แสดงข้อมูลที่ Error             
    except Exception as e:
      print('Error: Read Image')
      
      
# เรียงลำดับข้อมูลให้ถูกต้องแล้วดึงออกมาทีละค่า
for _i ,full_path_img_len in enumerate(natsort.natsorted(list_path_img)):
    
    print(full_path_img_len)

    # ตำแหน่งของ MOdel และตำแหน่งอื่นๆ
    paths = {
        'CHECKPOINT_PATH': os.path.join('model_plate(cocoNet)','models'), 
        'PIPELINE_CONFIG':os.path.join('model_plate(cocoNet)','models', 'pipeline.config'),
        'LABELMAP': os.path.join('model_plate(cocoNet)','annotations', 'label_map.pbtxt')
        }

    # โหลด PIPELINE ที่เราสร้างไว้
    configs = config_util.get_configs_from_pipeline_file(paths['PIPELINE_CONFIG'])
    detection_model = model_builder.build(model_config=configs['model'], is_training=False)

    # ย้อนกลับ checkpoint ที่สร้างไว้
    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], 'ckpt-2')).expect_partial()

    # สร้างชุดข้อมูลสำหรับการเรียกใช้งาน
    @tf.function
    def detect_fn(image):
        image, shapes = detection_model.preprocess(image)
        prediction_dict = detection_model.predict(image, shapes)
        detections = detection_model.postprocess(prediction_dict, shapes)
        return detections

    # เรียกใช้งาน label map
    category_index = label_map_util.create_category_index_from_labelmap(paths['LABELMAP'])

    # นำเข้ารูปภาพ
    image = cv2.imread(full_path_img_len)

    # แปลงรูปภาพเป็น array
    image_np = np.array(image)

    # แปลงรูปภาพเป็น tensor
    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections = detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    label_id_offset = 1
    img = image_np.copy()

    # แสดงผลลัพธ์ของ Model
    viz_utils.visualize_boxes_and_labels_on_image_array(
                img,
                detections['detection_boxes'],
                detections['detection_classes']+label_id_offset,
                detections['detection_scores'],
                category_index,
                use_normalized_coordinates=True,
                max_boxes_to_draw=5,
                min_score_thresh=.8,
                agnostic_mode=False)

    # เตรียมข้อมูลในส่วนของป้ายทะเบียน
    detections_threshold = 0.7
    scores = list(filter(lambda x: x> detections_threshold,detections['detection_scores']))
    boxes =detections['detection_boxes'][:len(scores)]
    classes=detections['detection_classes'][:len(scores)]

    # กำหนดค่าเริ่มต้นของป้ายทะเบียน
    width = img.shape[1]
    height = img.shape[0]

    # ตัดกรอบรูปภาพที่ต้องการ
    for idx, box in enumerate(boxes):
        roi = box*[height,width,height,width]
        region = img[int(roi[0]):int(roi[2]),int(roi[1]):int(roi[3])]
        reader = easyocr.Reader(['th'])
        ocr_result = reader.readtext(region)
        # print(ocr_result[0][1])
        # print(ocr_result[1][1])
        
        print(ocr_result[0][1])
        
        # #ลูปที่ใช้เปรียบเทียบความถูกต้องของข้อความที่ได้จากรูปภาพ
        # for _i ,city in enumerate (City_Ref):
        #         seq = difflib.SequenceMatcher(None,ocr_result[1][1],city)
        #         Accuracy = seq.ratio()*100
        #         if Accuracy >= 30.00:
        #             city_Ans.append({'ป้ายทะเบียน':ocr_result[0][1],'จังหวัด':city,'Acc':Accuracy})
                            

        # city_Ans.sort(key=myFunc, reverse=True)
    
# print(city_Ans[0])
# print(ocr_result)
    
cv2.imshow('plate',cv2.cvtColor(region,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()