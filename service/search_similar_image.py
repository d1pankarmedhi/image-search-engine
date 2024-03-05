from typing import List

from PIL import Image

from encoder.embedding import Embedding
from objectstore.store_s3 import S3Store
from utils.config_util import Config
from utils.utils_env import EnvironmentVariables
from vectorstore.store_pinecone import PineconeStore


def search_similar_images(top_k: int, image: Image):
    similar_images = list()
    config = Config.get_config()

    # fetch similar images from pinecone
    pc = PineconeStore(
        api_key=EnvironmentVariables.PINECONE_API_KEY,
        environment=EnvironmentVariables.PINECONE_ENVIRONMENT,
    )
    index = pc.load_index(
        index_name=config["pinecone_index_name"],
        dimension=512,
    )

    # convert image to embedding and get relevant results
    embedding = Embedding.encode_image(image)
    relevant_results = index.query(
        vector=embedding[0].tolist(), top_k=top_k, include_metadata=True
    )

    # fetch images from s3 bucket
    s3store = S3Store()
    client = s3store.get_client(
        access_key=EnvironmentVariables.AWS_S3_ACCESS_KEY,
        secret_key=EnvironmentVariables.AWS_S3_SECRET_ACCESS_KEY,
    )
    for result in relevant_results["matches"]:
        img = s3store.fetch_image(
            client,
            bucket_name=config["aws_s3_bucket_name"],
            key=result["metadata"]["image_key"],
        )
        similar_images.append(img)

    return similar_images
