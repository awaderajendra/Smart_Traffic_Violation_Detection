import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.title("🚦Smart Traffic Violation Detection System")

uploaded_file = st.file_uploader(
    "Upload Traffic Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    model = YOLO("yolov8n.pt")

    results = model(image)

    output = results[0].plot()

    st.image(output, caption="Detection Result", use_container_width=True)


