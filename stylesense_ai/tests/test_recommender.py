import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pandas as pd
from models.recommender import FashionRecommender

def test_recommendations_are_ranked_and_limited():
    rows=pd.DataFrame([{"id":1,"title":"Ideal","brand":"A","price":100,"style":"Minimal","occasion":"Office","colors":"Black,White","season":"Winter","popularity":90,"description":"x","image_path":"x","shopping_url":"x"},{"id":2,"title":"Other","brand":"B","price":400,"style":"Sporty","occasion":"Party","colors":"Red","season":"Summer","popularity":50,"description":"x","image_path":"x","shopping_url":"x"}])
    prefs={"style":"Minimal","occasion":"Office","preferred_colors":["Black"],"budget":150,"season":"Winter"}
    result=FashionRecommender(rows).recommend(prefs,limit=1)
    assert result[0]["title"]=="Ideal"
    assert result[0]["score"]>90
    assert "matches your minimal preference" in result[0]["explanation"]

def test_budget_score_penalizes_expensive_items():
    assert FashionRecommender._budget(100,100)==1
    assert FashionRecommender._budget(200,100)==0