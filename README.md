<div align='center'>
    <h1>🖼️ Image Search Engine</h1>
    <p>A vector-based image search engine powered by the Visual Transformer model type.</p>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) 
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) 
![Huggingface](https://img.shields.io/badge/Huggingface-%23FFD200.svg?style=for-the-badge&logo=&logoColor=white)
</div>

---

### 🔧 **Embedding Model**
We utilize the **CLIP** model 🤗 ([openai/clip-vit-base-patch32](openai/clip-vit-base-patch32)) to generate embedding vectors for images. These vectors are then stored in the **Pinecone** vector database, which facilitates the image search functionality.

- **How it works**:
  - The model generates embeddings for each image.
  - The images are stored in an **AWS S3** bucket across 4 classes: **Airplane**, **Dog**, **Cat**, and **Car** (120 images in total).
  - After generating embeddings, these vectors are saved to a **Pinecone** index, with links to their respective images stored as metadata.

- **Search process**:
  - The input image's vector embedding is generated.
  - The top-k relevant embeddings are fetched from the **Pinecone** database.
  - Finally, the images corresponding to the results are retrieved from the **S3** bucket using the metadata links.

![image](https://github.com/d1pankarmedhi/image-search-engine/assets/136924835/7e8aa331-a28e-41df-9614-5e39c5538638)
- **Fig 1**: Pipeline diagram

![image](https://github.com/d1pankarmedhi/image-search-engine/assets/136924835/19637f25-bc5f-4a90-982e-24efe6109a22)
- **Fig 2**: Search engine demo

---

### 🚀 **Getting Started**

Follow these simple steps to set up the project:

1️⃣ **Clone the Repository**  
   Run the following command to clone the project:
   ```bash
   git clone https://github.com/d1pankarmedhi/image-search-engine.git
   ```

2️⃣ **Set Up the Virtual Environment & Install Dependencies**  
   Create and activate a virtual environment, then install the required dependencies:
   ```bash
   python -m venv venv

   # Activate virtual environment
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows

   # Install dependencies
   pip install -r requirements.txt
   ```

3️⃣ **Configure the Project**  
   Open the `config.yaml` file and modify the necessary fields, such as the **S3** bucket name and the **Pinecone** index name.

5️⃣ **Run the Application**  
   Start the app with the following command:
   ```bash
   streamlit run app.py
   ```

---
