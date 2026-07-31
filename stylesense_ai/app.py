from pathlib import Path
import streamlit as st
from database.db_manager import DatabaseManager
from pages import analytics, home, recommendations, upload_photo, wardrobe

st.set_page_config(page_title="StyleSense AI",page_icon="✦",layout="wide",initial_sidebar_state="collapsed")
css=Path(__file__).parent.joinpath("assets/style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>",unsafe_allow_html=True)
pages=[("Home","⌂"),("Upload","⊕"),("Recommendations","✦"),("Wardrobe","♡"),("Analytics","◫")]
page_names={label for label,_ in pages}
requested_page=st.query_params.get("page")
if requested_page in page_names:
    st.session_state.page=requested_page
    del st.query_params["page"]
elif "page" not in st.session_state:
    st.session_state.page="Home"
    requested_page = st.query_params.get("page")
    valid_pages = {"Home", "Upload", "Recommendations", "Wardrobe", "Analytics"}
    if requested_page in valid_pages:
        st.session_state.page = requested_page
        st.query_params.clear()
db=DatabaseManager()
if st.session_state.page != "Home":
    st.markdown('<a class="page-back-link" href="?page=Home" target="_self">← Back</a>',unsafe_allow_html=True)
    with st.sidebar:
        st.markdown('<div class="brand"><div>✦</div><b>StyleSense</b><span>AI</span></div><p class="brand-copy">Your intelligent wardrobe</p>',unsafe_allow_html=True)
        if st.button("←   Back", key="nav_back", use_container_width=True): st.session_state.page = "Home"; st.rerun()
        for label,icon in pages:
            if st.button(f"{icon}   {label}",key=f"nav_{label}",type="primary" if st.session_state.page==label else "secondary",use_container_width=True): st.session_state.page=label; st.rerun()
        st.markdown('<div class="side-card"><span>STYLE PROFILE</span><b>Build your signature look</b><p>Upload a photo to unlock palette-aware recommendations.</p></div><div class="side-footer"><span class="avatar">SS</span><div><b>Style Explorer</b><small>Private profile</small></div></div>',unsafe_allow_html=True)
{"Home":lambda:home.render(),"Upload":lambda:upload_photo.render(db),"Recommendations":lambda:recommendations.render(db),"Wardrobe":lambda:wardrobe.render(db),"Analytics":lambda:analytics.render(db)}[st.session_state.page]()
