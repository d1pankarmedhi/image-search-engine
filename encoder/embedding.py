import matplotlib.pyplot as plt
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor, CLIPTokenizer


class Embedding:
    """
    A class for encoding images and text using the CLIP model.
    """

    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")
    model.to(device)

    @classmethod
    def encode_image(cls, image: Image):
        """
        Encode an image using the specified image processor and model, and return the image features as a numpy array.

        Args:
            image (Image): The input image to be encoded.

        Returns:
            np.ndarray: The encoded image features as a numpy array.
        """
        inputs = cls.processor(images=image, return_tensors="pt")["pixel_values"].to(
            cls.device
        )
        outputs = cls.model.get_image_features(inputs)
        np_embedding = outputs.cpu().detach().numpy()
        return np_embedding

    @classmethod
    def encode_text(cls, text: str):
        """
        Encode the input text using the tokenizer and model, and return the resulting numpy embedding.

        Args:
            text (str): The input text to be encoded.

        Returns:
            numpy array: The encoded text features as a numpy array.
        """
        inputs = cls.tokenizer(text, return_tensors="pt").to(cls.device)
        outputs = cls.model.get_text_features(**inputs)
        np_embedding = outputs.cpu().detach().numpy()
        return np_embedding
