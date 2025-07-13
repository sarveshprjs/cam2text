# cam2text/core.py

import cv2
from datetime import datetime
import os

def generate_activity_report(video_path, output_text_file="activity_log.txt"):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Error opening video file")

    # Define model paths
    model_dir = os.path.join(os.path.dirname(__file__), "models")
    prototxt_path = os.path.join(model_dir, "MobileNetSSD_deploy.prototxt.txt")
    caffemodel_path = os.path.join(model_dir, "MobileNetSSD_deploy.caffemodel")

    # Debug: print model paths
    print("[DEBUG] Checking model files:")
    print("  Prototxt path:", prototxt_path)
    print("  Caffe model path:", caffemodel_path)

    # Ensure model files exist
    if not os.path.exists(prototxt_path):
        raise FileNotFoundError(f"Missing model file: {prototxt_path}")
    if not os.path.exists(caffemodel_path):
        raise FileNotFoundError(f"Missing model file: {caffemodel_path}")

    # Load the pretrained model
    net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    classNames = ["background", "aeroplane", "bicycle", "bird", "boat",
                  "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                  "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                  "sofa", "train", "tvmonitor"]

    log_lines = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            class_id = int(detections[0, 0, i, 1])
            if confidence > 0.5 and class_id == 15:  # 'person'
                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
                time_str = str(datetime.utcfromtimestamp(timestamp).strftime("%H:%M:%S"))
                log_lines.append(f"Person detected at {time_str}")
                break

    cap.release()

    log_lines = sorted(set(log_lines))
    with open(output_text_file, "w") as f:
        for line in log_lines:
            f.write(line + "\n")

    return output_text_file
