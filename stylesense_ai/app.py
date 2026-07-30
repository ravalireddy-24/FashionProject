from pathlib import Path
import streamlit as st
from database.db_manager import DatabaseManager
from pages import analytics, home, recommendations, upload_photo, wardrobe

pages = {
    "Home": lambda: home.render(),
    "Upload": lambda: upload_photo.render(database),
    "Recommendations": lambda: recommendations.render(database),
    "Wardrobe": lambda: wardrobe.render(database),
    "Analytics": lambda: analytics.render(database),
}
pages.get(st.session_state.page, pages["Home"])()