import streamlit as st
from database.db_manager import DatabaseManager
from utils.ui import page_header

def render(db: DatabaseManager) -> None:
    page_header("YOUR COLLECTION", "The wardrobe you love.", "Saved looks, ready whenever inspiration calls.")
    favorites=db.favorites()
    if not favorites:
        st.markdown('<div class="empty glass"><b>♡</b><h2>Your wardrobe is waiting</h2><p>Save a recommendation and it will appear here.</p></div>',unsafe_allow_html=True); return
    columns=st.columns(3)
    for i,item in enumerate(favorites):
        with columns[i%3]:
            st.image(item.image_path,use_container_width=True)
            st.markdown(f'<div class="wardrobe-copy"><span>{item.brand}</span><h3>{item.title}</h3><b>${item.price:.0f}</b></div>',unsafe_allow_html=True)
            if st.button("Remove",key=f'remove_{item.outfit_id}',use_container_width=True): db.remove_favorite(item.outfit_id); st.rerun()