from __future__ import annotations
from typing import Any
import pandas as pd
from database.db_manager import DatabaseManager
from models.recommender import FashionRecommender
from utils.constants import OUTFITS_PATH

class RecommendationService:
    def __init__(self, database: DatabaseManager) -> None:
        self.database = database
        self.catalog = pd.read_csv(OUTFITS_PATH)
        self.catalog["image_path"] = self.catalog["image_path"].map(
            lambda path: str(OUTFITS_PATH.parents[2] / path)
        )
        self.recommender = FashionRecommender(self.catalog)

    def generate(self, preferences: dict[str, Any], image_embedding=None, persist: bool = True) -> list[dict[str, Any]]:
        results = self.recommender.recommend(preferences, 5, image_embedding)
        if persist:
            self.database.save_preferences(preferences)
            self.database.save_recommendations(results)
        return results