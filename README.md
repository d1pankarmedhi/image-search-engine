<div align='center'>
    <h1>Image Search Engine</h1>
    <p>A vector based image search engine using Visual Transformer model type.</p>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Huggingface](https://img.shields.io/badge/Huggingface-%23FFD200.svg?style=for-the-badge&logo=&logoColor=white)

</div>

---

### Embedding Model
Using the **CLIP** model 🤗 [openai/clip-vit-base-patch32](openai/clip-vit-base-patch32) to generate embedding vector for images, stored on a vector database, such as **Pinecone** to facilitate search capabilities.

![image](https://github.com/d1pankarmedhi/image-search-engine/assets/136924835/7e8aa331-a28e-41df-9614-5e39c5538638)
- Fig: Pipeline diagram

With 4 classes, including **Airplane, Dog, Cat and Car**, there are around 120 images (30 each) in total. These images are stored in an **AWS S3** bucket. After generating embeddings for each image, these embeddings are stored on a **Pinecone** index with their respective **S3** links as metadata.

The vector embedding of the input image is generated and the relevant top-k embeddings are fetched from the **Pinecone** database. Once the results are obtained, the corresponding images are fetched from the **S3** bucket using the links stored as metadata.

![image](https://github.com/d1pankarmedhi/image-search-engine/assets/136924835/19637f25-bc5f-4a90-982e-24efe6109a22)
- Fig: Search engine demo

## Getting started
1. Clone repository
2. Create virtual env and install dependencies
   ```bash
   python -m venv venv

   source venv/bin/activate # linux
   venv\Scripts\activate # windows

   pip install -r requirements.txt
   ```
3. Modify the `config.yaml` file and add the necessary fields like S3 bucket name, pinecone index name, etc. 
4. Run the application using
   ```bash
   streamlit run app.py
   ```



