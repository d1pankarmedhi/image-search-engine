from dotenv import load_dotenv
import os 
load_dotenv()

class EnvironmentVariables:
    PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT=os.getenv("PINECONE_ENVIRONMENT")
    AWS_S3_ACCESS_KEY=os.getenv("AWS_S3_ACCESS_KEY")
    AWS_S3_SECRET_ACCESS_KEY=os.getenv("AWS_S3_SECRET_ACCESS_KEY")
    PINECONE_INDEX_NAME=os.getenv("PINECONE_INDEX_NAME")