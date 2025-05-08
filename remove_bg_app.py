import os
import streamlit as st
from PIL import Image
from rembg import remove
import io

os.makedirs("original", exist_ok=True)

st.title("Image Background Remover app")
uploaded_file = st.file_uploader("Upload a image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    original_path = os.path.join("original", uploaded_file.name)
    with open(original_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Image saved to: {original_path}")

    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    with st.spinner("Removing bg..."):
        output = remove(file_bytes)

    result_image = Image.open(io.BytesIO(output))
    st.image(result_image, caption="Image Without Background", use_container_width=True)

    st.download_button("Download Transparent Image", output, file_name="no_bg.png")
