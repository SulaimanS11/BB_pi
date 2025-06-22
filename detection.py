# import tensorflow as tf
# import numpy as np
# import cv2

# interpreter = tf.lite.Interpreter(model_path='models/mobilenet_ssd.tflite')
# interpreter.allocate_tensors()

# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# def detect_objects(frame):
#     input_data = cv2.resize(frame, (300, 300))
#     input_data = np.expand_dims(input_data, axis=0)
#     interpreter.set_tensor(input_details[0]['index'], input_data)
#     interpreter.invoke()

#     boxes = interpreter.get_tensor(output_details[0]['index'])[0]
#     classes = interpreter.get_tensor(output_details[1]['index'])[0]
#     scores = interpreter.get_tensor(output_details[2]['index'])[0]

#     return boxes, classes, scores