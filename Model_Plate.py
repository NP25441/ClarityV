import os, cv2
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import numpy as np

class Model_Plate:
    def __init__ (self):
        pass

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
        image, shapes = Model_Plate.detection_model.preprocess(image)
        prediction_dict = Model_Plate.detection_model.predict(image, shapes)
        detections = Model_Plate.detection_model.postprocess(prediction_dict, shapes)
        return detections

    # เรียกใช้งาน label map
    category_index = label_map_util.create_category_index_from_labelmap(paths['LABELMAP'])
    
    def model_plate(self,index,full_path_img_len):

        # นำเข้ารูปภาพ
        image = cv2.imread(full_path_img_len)

        # แปลงรูปภาพเป็น array
        image_np = np.array(image)

        # แปลงรูปภาพเป็น tensor
        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        detections = Model_Plate.detect_fn(input_tensor)

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
                    Model_Plate.category_index,
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
        
        plate_img = cv2.cvtColor(region,cv2.COLOR_BGR2RGB)
        cv2.imwrite("Snapshot_Plate\%d.jpg" % index, plate_img)  
        # print('Saved palte: ', index)
        
        
        return plate_img
            
        # cv2.imshow('plate',plate_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()