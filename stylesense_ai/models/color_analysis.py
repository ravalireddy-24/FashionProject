from __future__ import annotations
import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

COLOR_LIBRARY = {"Black": (25,25,28), "White": (238,238,235), "Beige": (210,190,160), "Brown": (110,75,55), "Gray": (130,130,135), "Navy": (35,50,80), "Blue": (60,110,175), "Green": (65,115,80), "Red": (175,55,60), "Pink": (210,115,145), "Purple": (120,75,160), "Orange": (220,125,55), "Yellow": (220,190,75)}

class ColorAnalyzer:
    def extract(self, image: Image.Image, count: int = 4) -> list[dict[str, object]]:
        rgb = np.asarray(image.convert("RGB").resize((120, 120)))
        pixels = rgb.reshape(-1, 3)
        model = KMeans(n_clusters=count, random_state=42, n_init=5).fit(pixels)
        labels, counts = np.unique(model.labels_, return_counts=True)
        order = labels[np.argsort(counts)[::-1]]
        return [{"name": self.nearest_name(model.cluster_centers_[index]), "hex": "#" + "".join(f"{int(v):02x}" for v in model.cluster_centers_[index]), "percentage": round(float(counts[np.where(labels == index)[0][0]] / len(pixels) * 100), 1)} for index in order]

    @staticmethod
    def nearest_name(rgb: np.ndarray) -> str:
        return min(COLOR_LIBRARY, key=lambda name: np.linalg.norm(rgb - np.array(COLOR_LIBRARY[name])))

    def clothing_palette(self, image: Image.Image) -> list[dict[str, object]]:
        array = np.asarray(image.convert("RGB"))
        h, w = array.shape[:2]
        crop = array[int(h*.18):int(h*.88), int(w*.15):int(w*.85)]
        return self.extract(Image.fromarray(cv2.GaussianBlur(crop, (5,5), 0)), 3)