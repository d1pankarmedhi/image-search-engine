# image-search-engine
🔎 A vector space search engine for similar images.

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



