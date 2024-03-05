from io import BytesIO
from typing import List

import boto3
from PIL import Image


class S3Store:
    def __init__(self) -> None:
        pass

    def get_client(
        self, access_key: str, secret_key: str, region_name: str = "ap-south-1"
    ):
        """
        Retrieves a client for interacting with the AWS S3 service.

        Args:
            access_key (str): The access key for AWS authentication.
            secret_key (str): The secret key for AWS authentication.
            region_name (str, optional): The AWS region name. Defaults to "ap-south-1".

        Returns:
            botocore.client.S3: A client for interacting with the AWS S3 service.
        """
        client = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name,
        )
        return client

    def fetch_image(self, client, bucket_name: str, key: str) -> Image:
        """
        Fetches an image from the specified bucket using the provided client, bucket name, and key, and returns the image object.

        Args:
            client: The client object used to interact with the AWS S3 service.
            bucket_name (str): The name of the bucket from which to fetch the image.
            key (str): The key of the image object within the specified bucket.

        Returns:
            Image: The image object fetched from the specified bucket.
        """
        file_byte_string = client.get_object(Bucket=bucket_name, Key=key)["Body"].read()
        return Image.open(BytesIO(file_byte_string))

    def list_buckets(self, client):
        """
        List S3 buckets using the provided client.

        Args:
            self: The object instance.
            client: The client object used to list the buckets.

        Returns:
            None
        """
        clientResponse = client.list_buckets()
        # Print the bucket names one by one
        print("Available S3 buckets")
        for bucket in clientResponse["Buckets"]:
            print(f'Bucket Name: {bucket["Name"]}')

    def list_objects(self, client, bucket_name: str) -> List:
        """
        List all objects in a bucket

        Args:
            client (boto3.client): boto3 client
            bucket_name (str): name of the bucket

        Returns:
            List: list of objects in the bucket
        """
        response = client.list_objects_v2(Bucket=bucket_name)
        return response.get("Contents")
