import os

import streamlit as st
from PIL import Image

from service.search_similar_image import search_similar_images


def main():
    st.set_page_config(layout="wide", page_title="Image Search Engine", page_icon="🔎")
    # markdown title
    st.markdown(
        """
    <h1 style='text-align: center;'>Image Search Engine</h1>
    """,
        unsafe_allow_html=True,
    )

    info_expander = st.expander("🤔 How does it work?")
    info_expander.markdown("""
    Upon uploading the image, the **[CLIP Vit Base patch-32](https://huggingface.co/openai/clip-vit-base-patch32)** model is used to extract image features from the image. The image features are then used to search for similar images in the vector dataset. The dataset embeddings are stored in the Pinecone database with the **AWS S3** image links as metadata for each entry. 
                           
    The top k results are then fetched from the Pinecone database along with their respective AWS S3 links. These images are fetched from S3 bucket and displayed in the app.   

    """)

    number_of_images_expander = st.sidebar.expander("🥇 Number of image", expanded=True)
    num_of_images = number_of_images_expander.slider(
        "", min_value=1, max_value=6, value=3
    )
    upload_image_expander = st.sidebar.expander("📃 Upload image", expanded=True)
    uploaded_img = upload_image_expander.file_uploader(" ", type=["png", "jpg", "jpeg"])
    submit_btn = st.sidebar.button("Search")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True, height=300):
            st.markdown(
                """<h3 style='text-align: center;'>Uploaded Image</h3>""",
                unsafe_allow_html=True,
            )
            if uploaded_img:
                # show uploaded image
                st.image(uploaded_img)
    with col2:
        with st.container(border=True, height=300):
            st.markdown(
                """<h3 style='text-align: center;'>Similar Images</h3>""",
                unsafe_allow_html=True,
            )
            if submit_btn:
                # convert uploaded_image to PIL.Image
                img = Image.open(uploaded_img)
                similar_images = search_similar_images(top_k=num_of_images, image=img)

                cols = st.columns(3)

                for i, img in enumerate(similar_images):
                    cols[i % 3].image(img)

    with st.container(border=True, height=300):
        st.markdown(
            """<h3 style='text-align: center;'>Sample Images</h3>""",
            unsafe_allow_html=True,
        )
        sample_images = os.listdir("sample_imgs")
        sample_images = [Image.open(f"sample_imgs/{img}") for img in sample_images]
        cols = st.columns(len(sample_images))
        for i, img in enumerate(sample_images):
            cols[i % len(sample_images)].image(img, use_column_width=True)


if __name__ == "__main__":
    main()
