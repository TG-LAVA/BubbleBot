from ultralytics import YOLO

# Load a model
# model = YOLO("yolo11n-seg.yaml")  # build a new model from YAML
model = YOLO("yolo11n-seg.pt")  # load a pretrained model (recommended for training)
# model = YOLO("yolov8n-seg.yaml").load("yolov8n-seg.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="red_cup.yaml", epochs=100, imgsz=640)

