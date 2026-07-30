from pathlib import Path
import streamlit as st
from database.db_manager import DatabaseManager
from pages import analytics, home, recommendations, upload_photo, wardrobe

st.set_page_config(page_title="StyleSense AI",page_icon="✦",layout="wide",initial_sidebar_state="expanded")
css=Path(__file__).parent.joinpath("assets/style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>",unsafe_allow_html=True)
if "page" not in st.session_state: st.session_state.page="Home"
db=DatabaseManager()
with st.sidebar:
    st.markdown('<div class="brand"><div>✦</div><b>StyleSense</b><span>AI</span></div><p class="brand-copy">Your intelligent wardrobe</p>',unsafe_allow_html=True)
    pages=[("Home","⌂"),("Upload","⊕"),("Recommendations","✦"),("Wardrobe","♡"),("Analytics","◫")]
    for label,icon in pages:
        if st.button(f"{icon}   {label}",key=f"nav_{label}",type="primary" if st.session_state.page==label else "secondary",use_container_width=True): st.session_state.page=label; st.rerun()
    st.markdown('<div class="side-card"><span>STYLE PROFILE</span><b>Build your signature look</b><p>Upload a photo to unlock palette-aware recommendations.</p></div><div class="side-footer"><span class="avatar">SS</span><div><b>Style Explorer</b><small>Private profile</small></div></div>',unsafe_allow_html=True)
{"Home":lambda:home.render(),"Upload":lambda:upload_photo.render(db),"Recommendations":lambda:recommendations.render(db),"Wardrobe":lambda:wardrobe.render(db),"Analytics":lambda:analytics.render(db)}[st.session_state.page]()