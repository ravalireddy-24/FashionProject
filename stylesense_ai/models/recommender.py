from __future__ import annotations
from typing import Any
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
from utils.constants import WEIGHTS
from utils.helpers import parse_list

class FashionRecommender:
    def __init__(self, outfits: pd.DataFrame) -> None:
        self.outfits = outfits.copy()

    @staticmethod
    def _exact(value: str, preferred: str) -> float:
        return 1.0 if value.casefold() == preferred.casefold() else 0.2

    @staticmethod
    def _color(colors: object, preferred: list[str]) -> float:
        available = {x.casefold() for x in parse_list(colors)}
        wanted = {x.casefold() for x in preferred}
        return len(available & wanted) / max(1, len(wanted))

    @staticmethod
    def _budget(price: float, budget: float) -> float:
        if price <= budget:
            return 1.0
        return max(0.0, 1 - (price - budget) / max(budget, 1))

    def recommend(self, preferences: dict[str, Any], limit: int = 5, image_embedding: np.ndarray | None = None) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        for _, row in self.outfits.iterrows():
            components = {"style": self._exact(str(row.style), preferences["style"]), "occasion": self._exact(str(row.occasion), preferences["occasion"]), "color": self._color(row.colors, preferences["preferred_colors"]), "budget": self._budget(float(row.price), float(preferences["budget"])), "season": 1.0 if preferences["season"] == "All Season" or str(row.season) in (preferences["season"], "All Season") else 0.25}
            score = sum(components[key] * WEIGHTS[key] for key in WEIGHTS)
            popularity_boost = min(float(row.popularity) / 100, 1) * 0.03
            visual_score = 0.0
            if image_embedding is not None and "embedding" in row and isinstance(row.embedding, np.ndarray):
                visual_score = float(cosine_similarity([image_embedding], [row.embedding])[0,0]) * 0.05
            score = min(1.0, score + popularity_boost + visual_score)
            colors = parse_list(row.colors)
            explanation = f"This outfit matches your {preferences['style'].lower()} preference, {', '.join(colors[:2]).lower()} color palette and {preferences['occasion'].lower()} occasion."
            item = row.to_dict() | {"score": round(score * 100, 1), "component_scores": {k: round(v * 100, 1) for k,v in components.items()}, "explanation": explanation}
            results.append(item)
        return sorted(results, key=lambda x: (x["score"], x["popularity"]), reverse=True)[:limit]