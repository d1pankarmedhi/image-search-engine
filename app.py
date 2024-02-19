import streamlit as st 
import os 
from PIL import Image

st.title("🔎 Vector space Image search")


images = os.listdir("data")

with st.sidebar.expander("Display number of images"):
    n_imgs = st.sidebar.slider("Display number of image", min_value=1, max_value=6)
    
with st.sidebar.expander("Upload image"):
    uploaded_img = st.sidebar.file_uploader(" ", type="PDF")
    
with st.sidebar.expander("Select Model"):
    st.write("Select")

cols = st.columns(3)


for i, img in enumerate(images):
    img_path = os.path.join("data", img)
    cols[i%3].image(Image.open(img_path))
    