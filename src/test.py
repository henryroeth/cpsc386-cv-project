from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("C:/Users/henry/Projects/cpsc386-cv-project/runs/classify/train/weights/best.pt")

# Load an image for inference
image_path = "dataset/test/Pleurotus_ostreatus/Pleurotus_ostreatus_5.jpg"  
image = cv2.imread(image_path)  # load the image

# Perform inference
results = model(image)