from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="traffic.jpg",
    save=True,
    conf=0.5
)

print("Prediction Completed")