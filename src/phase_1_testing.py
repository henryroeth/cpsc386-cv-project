from ultralytics import YOLO
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys

# Choose a pretrained model for either detection or classification
modelChoice = int(input("Choose a type of model (1 for detection, 2 for classification): "))

# Load the chosen model
if(modelChoice == 1):
    model = YOLO("yolov8n.pt") # detection model
elif(modelChoice == 2):
    model = YOLO("yolo11n-cls.pt") # classification model
else:
    sys.exit("Error: You must choose a valid option.") # exit with error message

# Choose the path to the image file
app = QApplication(sys.argv)
source, _ = QFileDialog.getOpenFileName(
    None,
    "Select Image",
    "",
    "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
)

# Run inference on the source
results = model(source, show=True) # list of Results objects

# Show the results of the first element
results[0].show()