from __future__ import annotations
import cv2
import numpy as np
from PIL import Image

class ImageEmbedder:
    """Deterministic visual descriptor combining HSV histograms and edge geometry."""
    dimensions = 112

    def embed(self, image: Image.Image) -> np.ndarray:
        rgb = np.asarray(image.convert("RGB").resize((224, 224)))
        hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [12, 8], [0, 180, 0, 256]).flatten()
        gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 80, 160)
        grid = cv2.resize(edges, (4, 4)).astype(np.float32).flatten()
        vector = np.concatenate([hist.astype(np.float32), grid])
        norm = np.linalg.norm(vector)
        return vector / norm if norm else vector