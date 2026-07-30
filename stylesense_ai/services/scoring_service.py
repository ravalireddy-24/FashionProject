from __future__ import annotations
from typing import Any
from utils.constants import WEIGHTS

class ScoringService:
    @staticmethod
    def weighted_score(component_scores: dict[str, float]) -> float:
        return round(sum(component_scores.get(name, 0) * weight for name, weight in WEIGHTS.items()), 2)

    @staticmethod
    def breakdown(component_scores: dict[str, Any]) -> list[tuple[str, float]]:
        return [(name.title(), float(component_scores.get(name, 0))) for name in WEIGHTS]