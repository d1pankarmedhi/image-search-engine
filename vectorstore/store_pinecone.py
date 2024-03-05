import time
import uuid
from typing import Dict, Optional

from pinecone import Pinecone, PodSpec, ServerlessSpec

from logger.logger import get_logger

logger = get_logger(__name__)


class PineconeStore:
    def __init__(self, api_key: str, environment: str) -> None:
        self.api_key = api_key
        self.environment = environment
        self.pinecone = Pinecone(api_key=api_key)

    def load_index(
        self,
        index_name: str = "image-search-engine",
        dimension: int = 512,
        use_serverless: bool = False,
        cloud: str = "aws",
        region: str = "us-west-2",
    ):
        try:
            if use_serverless:
                spec = ServerlessSpec(cloud="aws", region="us-west-2")
            else:
                spec = PodSpec(environment=self.environment)

            existing_indexes = self.list_indexes()

            # check if index already exists (it shouldn't if this is first time)
            if index_name not in existing_indexes:
                logger.info(f"Index not found - creating index {index_name}")

                # if does not exist, create index
                self.pinecone.create_index(
                    index_name,
                    dimension=dimension,  # dimensionality of minilm
                    metric="cosine",
                    spec=spec,
                )
                # wait for index to be initialized
                while not self.pinecone.describe_index(index_name).status["ready"]:
                    time.sleep(1)
            logger.info(f"Index {index_name} created")

            # connect to index
            index = self.pinecone.Index(index_name)
            return index
        except Exception as e:
            logger.error(f"{e}")

    def upsert_data(self, index, data, namespace: Optional[str] = "ns1"):
        for doc in data:
            index.upsert(
                vectors=[
                    {
                        "id": str(uuid.uuid4()),
                        "values": doc["embedding"],
                        "metadata": {"image_key": doc["image_key"]},
                    }
                ],
                namespace=namespace,
            )
        logger.info(f"Data loaded")

    def list_indexes(self):
        existing_indexes = [
            index_info["name"] for index_info in self.pinecone.list_indexes()
        ]
        return existing_indexes
