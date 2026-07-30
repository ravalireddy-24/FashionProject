from __future__ import annotations
from io import BytesIO
from pathlib import Path
from typing import BinaryIO
import numpy as np
from PIL import Image, ImageStat, UnidentifiedImageError
from sklearn.metrics.pairwise import cosine_similarity
from models.color_analysis import ColorAnalyzer
from models.image_embedding import ImageEmbedder
from utils.constants import UPLOAD_DIR
from utils.helpers import safe_filename

class ImageService:
    def __init__(self) -> None:
        self.colors = ColorAnalyzer()
        self.embedder = ImageEmbedder()
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    def validate(self, content: bytes) -> Image.Image:
        if len(content) > 20 * 1024 * 1024:
            raise ValueError("Image must be smaller than 20 MB.")
        try:
            image = Image.open(BytesIO(content))
            image.verify()
            image = Image.open(BytesIO(content)).convert("RGB")
        except (UnidentifiedImageError, OSError) as error:
            raise ValueError("The uploaded file is not a valid image.") from error
        if image.width < 100 or image.height < 100:
            raise ValueError("Image must be at least 100 × 100 pixels.")
        return image

    def save(self, uploaded: BinaryIO, filename: str) -> Path:
        content = uploaded.read()
        image = self.validate(content)
        path = UPLOAD_DIR / safe_filename(filename)
        image.save(path, quality=92)
        return path

    def analyze(self, image_or_path: Image.Image | str | Path) -> dict[str, object]:
        image = image_or_path if isinstance(image_or_path, Image.Image) else Image.open(image_or_path).convert("RGB")
        palette = self.colors.clothing_palette(image)
        category = self.estimate_category(image)
        return {"dominant_colors": palette, "category": category, "embedding": self.embedder.embed(image).tolist()}

    @staticmethod
    def estimate_category(image: Image.Image) -> str:
        ratio = image.width / image.height
        brightness = sum(ImageStat.Stat(image.resize((50,50))).mean) / 3
        if ratio > 1.15: return "Accessories"
        if ratio < 0.68: return "Dress"
        return "Outerwear" if brightness < 95 else "Top & Bottom"

    @staticmethod
    def similar(query: np.ndarray, catalog: list[np.ndarray], limit: int = 5) -> list[int]:
        if not catalog: return []
        scores = cosine_similarity([query], catalog)[0]
        return np.argsort(scores)[::-1][:limit].tolist()