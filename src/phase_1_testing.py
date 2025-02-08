from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n-cls.pt")

# Define path to the image file
source = "C:/Users/henry/cpsc386-cv-project/data/closeup-shot-black-labrador-playing-grass-surrounded-by-greenery.jpg"

# Run inference on the source
results = model(source) # list of Results objects

# Access first element of the list
result = results[0]

# Display the result
result.show()