import tkinter as tk
from tkinter import filedialog
import os
from ultralytics import YOLO

# Function to select model and image files using tkinter
def select_files():
    # Initialize tkinter window
    root = tk.Tk()
    root.withdraw()  # Close the root window (no need to show a blank window)
    
    # Open file dialog to select the YOLOv8 model (.pt file)
    model_path = filedialog.askopenfilename(title="Select YOLOv8 Model", 
                                            filetypes=[("PyTorch Model", "*.pt")])
    
    # Open file dialog to select the image file
    image_path = filedialog.askopenfilename(title="Select Image for Detection", 
                                            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.tif")])
    
    # Return the selected file paths
    return model_path, image_path

# Get model and image paths from user
model_path, image_path = select_files()

# Ensure paths are correct
if not model_path or not image_path:
    print("Model or image file not selected!")
else:
    # Load the selected YOLO model
    model = YOLO(model_path)

    # Perform detection on the selected image
    results = model(image_path)

     # Handle case where results is a list (usually when a batch of images is processed)
    if isinstance(results, list):
        # Access the first result
        result = results[0]
        # Show the detection results (on the first image)
        result.show()
    else:
        # If results is not a list (just a single result), show it directly
        results.show()
