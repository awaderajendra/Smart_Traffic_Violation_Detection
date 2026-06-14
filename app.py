import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

image = cv2.imread("traffic.jpg")

if image is None:
    print("traffic.jpg file not found")
    exit()

results = model(image)

output_image = results[0].plot()

cv2.imshow("Smart Traffic Violation Detection", output_image)

cv2.waitKey(0)

cv2.destroyAllWindows()