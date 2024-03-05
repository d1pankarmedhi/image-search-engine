<div align='center'>
    <h1>Image Search Engine</h1>
    <p>A vector based image search engine using Visual Transformer model type.</p>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Huggingface](https://img.shields.io/badge/Huggingface-%23FFD200.svg?style=for-the-badge&logo=&logoColor=white)

</div>

---

### Embedding Model
Using the **CLIP** model 🤗 [openai/clip-vit-base-patch32](openai/clip-vit-base-patch32) to generate embedding vector for images, stored on a vector database, such as **Pinecone** to facilitate search capabilities.



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



