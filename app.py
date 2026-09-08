import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(
    page_title="AquaGuard AI - Marine Debris Detection",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 AquaGuard AI")
st.subheader("AI-Powered Underwater Marine Debris Detection and Monitoring System")
st.info(
    "Prototype demonstration: upload an underwater image to generate a visual "
    "marine-debris monitoring report. AI model integration can be added in the "
    "next development stage."
)

uploaded = st.file_uploader(
    "Upload an underwater image",
    type=["jpg", "jpeg", "png"]
)

def prototype_analysis(image):
    """Visual prototype analysis. This is not a trained object detector."""
    arr = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    brightness = float(gray.mean())

    # Simple image-quality/environment indicators for prototype demonstration.
    contrast = float(gray.std())
    blue_ratio = float(arr[:, :, 2].mean() / (arr.mean() + 1e-6))

    if brightness < 75:
        quality = "Low-light underwater image"
    elif brightness < 130:
        quality = "Moderate-light underwater image"
    else:
        quality = "Good-light underwater image"

    if contrast < 35:
        visibility = "Low"
    elif contrast < 65:
        visibility = "Moderate"
    else:
        visibility = "High"

    if blue_ratio > 1.08:
        environment = "Blue-dominant underwater scene"
    else:
        environment = "Mixed-color underwater scene"

    return quality, visibility, environment

if uploaded:
    image = Image.open(uploaded).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Uploaded Image")
        st.image(image, use_container_width=True)

    with col2:
        st.markdown("### Environmental Analysis")
        quality, visibility, environment = prototype_analysis(image)

        st.metric("Image Visibility", visibility)
        st.write("**Image condition:**", quality)
        st.write("**Scene indication:**", environment)

        st.warning(
            "No trained marine-debris detector is bundled with this starter prototype. "
            "Object labels should only be displayed after a validated detection model "
            "has been trained/evaluated."
        )

    st.markdown("---")
    st.markdown("### Monitoring Workflow")
    st.write(
        "Underwater Image → Image Processing → AI Marine Debris Detector → "
        "Debris Classification → Environmental Analysis → Monitoring Report"
    )

    st.markdown("### Responsible AI")
    st.write(
        "AI predictions should be treated as decision support. Results require "
        "human verification, especially when image quality is poor or objects are "
        "partially occluded. The system does not require personal or sensitive data."
    )
else:
    st.markdown("### How it works")
    st.write(
        "1. Upload an underwater image.  \n"
        "2. The prototype checks image conditions.  \n"
        "3. A validated object-detection model can be connected for debris detection.  \n"
        "4. Results can then be summarized for environmental monitoring."
    )
