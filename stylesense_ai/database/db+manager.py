from __future__ import annotations
from datetime import datetime
from typing import Any
from sqlalchemy import DateTime, Float, Integer, String, Text, create_engine, delete, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from utils.constants import DATABASE_PATH
from utils.helpers import json_dumps

class Base(DeclarativeBase):
    pass

class Favorite(Base):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    outfit_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    title: Mapped[str] = mapped_column(String(160))
    brand: Mapped[str] = mapped_column(String(120))
    price: Mapped[float] = mapped_column(Float)
    image_path: Mapped[str] = mapped_column(Text)
    saved_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class UserPreference(Base):
    __tablename__ = "user_preferences"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    occasion: Mapped[str] = mapped_column(String(80))
    style: Mapped[str] = mapped_column(String(80))
    budget: Mapped[float] = mapped_column(Float)
    preferred_colors: Mapped[str] = mapped_column(Text)
    season: Mapped[str] = mapped_column(String(40))
    gender: Mapped[str] = mapped_column(String(40))
    favorite_brands: Mapped[str] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    outfit_id: Mapped[int] = mapped_column(Integer, index=True)
    score: Mapped[float] = mapped_column(Float)
    explanation: Mapped[str] = mapped_column(Text)
    component_scores: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Feedback(Base):
    __tablename__ = "feedback"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    recommendation_id: Mapped[int] = mapped_column(Integer, index=True)
    helpful: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class ImageAnalysis(Base):
    __tablename__ = "image_analyses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    image_path: Mapped[str] = mapped_column(Text)
    dominant_colors: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(80))
    embedding: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class DatabaseManager:
    def __init__(self, url: str | None = None) -> None:
        DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.engine = create_engine(url or f"sqlite:///{DATABASE_PATH}", future=True)
        self.Session = sessionmaker(self.engine, expire_on_commit=False)
        Base.metadata.create_all(self.engine)

    def save_preferences(self, preferences: dict[str, Any]) -> None:
        with self.Session.begin() as session:
            session.add(UserPreference(**{**preferences, "preferred_colors": json_dumps(preferences["preferred_colors"]), "favorite_brands": json_dumps(preferences["favorite_brands"])}))

    def save_recommendations(self, rows: list[dict[str, Any]]) -> None:
        with self.Session.begin() as session:
            for row in rows:
                session.add(Recommendation(outfit_id=int(row["id"]), score=float(row["score"]), explanation=row["explanation"], component_scores=json_dumps(row["component_scores"])))

    def add_favorite(self, outfit: dict[str, Any]) -> None:
        with self.Session.begin() as session:
            exists = session.scalar(select(Favorite).where(Favorite.outfit_id == int(outfit["id"])))
            if not exists:
                session.add(Favorite(outfit_id=int(outfit["id"]), title=outfit["title"], brand=outfit["brand"], price=float(outfit["price"]), image_path=outfit["image_path"]))

    def remove_favorite(self, outfit_id: int) -> None:
        with self.Session.begin() as session:
            session.execute(delete(Favorite).where(Favorite.outfit_id == outfit_id))

    def favorites(self) -> list[Favorite]:
        with self.Session() as session:
            return list(session.scalars(select(Favorite).order_by(Favorite.saved_at.desc())))

    def add_feedback(self, recommendation_id: int, helpful: bool, comment: str = "") -> None:
        with self.Session.begin() as session:
            session.add(Feedback(recommendation_id=recommendation_id, helpful=int(helpful), comment=comment))

    def save_analysis(self, analysis: dict[str, Any]) -> None:
        with self.Session.begin() as session:
            session.add(ImageAnalysis(image_path=analysis["image_path"], dominant_colors=json_dumps(analysis["dominant_colors"]), category=analysis["category"], embedding=json_dumps(analysis["embedding"])))

    def analytics(self) -> dict[str, Any]:
        with self.Session() as session:
            recommendations = list(session.scalars(select(Recommendation)))
            feedback = list(session.scalars(select(Feedback)))
            favorites = list(session.scalars(select(Favorite)))
        helpful = sum(item.helpful for item in feedback)
        return {"recommendations": recommendations, "feedback": feedback, "favorites": favorites, "average_score": sum(r.score for r in recommendations) / len(recommendations) if recommendations else 0, "accuracy": (helpful / len(feedback) * 100) if feedback else 0}