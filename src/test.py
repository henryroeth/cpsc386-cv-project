from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("/home/henry/Projects/cpsc386-cv-project/runs/classify/train/weights/best.pt")

# Load an image for inference
image_path = "/home/henry/Projects/cpsc386-cv-project/dataset/test/Coprinus_comatus/Coprinus_comatus_11.jpg"  
image = cv2.imread(image_path)  # load the image

# Perform inference
results = model(image)