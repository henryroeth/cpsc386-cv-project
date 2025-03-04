from ultralytics import YOLO

# Load the model
print("Choose the model:")
print("1. Pre-trained model (yolov8n.pt)")
print("2. Model from scratch (yolov8n.yaml)")

choice = input("Enter your choice (1 or 2): ") # define the choice of model

if choice == '1':
    model = YOLO("yolov8n.pt")  # load pre-trained model
elif choice == '2':
    model = YOLO("yolov8n.yaml")  # load model from scratch
else:
    print("Invalid choice. Please enter 1 or 2.")

# Use the model
training_passes = int(input("Define the number of epochs: ")) # define the number of times the model is trained with the annotated dataset (epochs)
results = model.train(data="src/detect_config.yaml", epochs=training_passes)