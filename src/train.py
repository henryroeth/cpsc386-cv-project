from ultralytics import YOLO

# Load pre-trained YOLOv8 classification model
model = YOLO("yolov8n-cls.pt")  

# Train the model with specific metrics
model.train(data="C:/Users/henry/Projects/cpsc386-cv-project/dataset/", epochs=30, imgsz=640, batch=16, patience=5)

