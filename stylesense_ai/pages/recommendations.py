mport streamlit as st
from database.db_manager import DatabaseManager
from services.recommendation_service import RecommendationService
from utils.constants import DEFAULT_PREFERENCES, GENDERS, OCCASIONS, SEASONS, STYLES

def render(db: DatabaseManager) -> None:
    st.markdown('<div class="page-title"><span>02 / CURATE</span><h1>Looks selected for you.</h1><p>Fine-tune your preferences, then explore your highest-scoring matches.</p></div>',unsafe_allow_html=True)
    with st.expander("Personalize your edit", expanded="recommendations" not in st.session_state):
        a,b,c=st.columns(3)
        occasion=a.selectbox("Occasion",OCCASIONS,index=OCCASIONS.index(DEFAULT_PREFERENCES["occasion"]))
        style=b.selectbox("Style",STYLES,index=STYLES.index(DEFAULT_PREFERENCES["style"]))
        budget=c.slider("Maximum budget",50,500,int(DEFAULT_PREFERENCES["budget"]),10,format="$%d")
        d,e,f=st.columns(3)
        season=d.selectbox("Season",SEASONS,index=SEASONS.index(DEFAULT_PREFERENCES["season"]))
        gender=e.selectbox("Collection",GENDERS,index=2)
        brands=f.text_input("Favorite brands","Aster & Row, Studio Nine")
        colors=st.multiselect("Preferred colors",["Black","White","Beige","Brown","Gray","Navy","Blue","Green","Red","Pink","Purple","Orange","Yellow"],default=DEFAULT_PREFERENCES["preferred_colors"])
        generate=st.button("Generate my edit ✦",type="primary",use_container_width=True)
    if generate or "recommendations" not in st.session_state:
        prefs={"occasion":occasion,"style":style,"budget":float(budget),"preferred_colors":colors,"season":season,"gender":gender,"favorite_brands":[x.strip() for x in brands.split(",") if x.strip()]}
        embedding=st.session_state.get("analysis",{}).get("embedding")
        st.session_state.recommendations=RecommendationService(db).generate(prefs,embedding)
    items=st.session_state.get("recommendations",[])
    st.markdown(f'<div class="results-bar"><b>{len(items)} exceptional matches</b><span>Ranked by StyleSense weighted scoring</span></div>',unsafe_allow_html=True)
    for index,item in enumerate(items):
        image,details,action=st.columns([1.05,2.2,.7],gap="large")
        with image: st.image(item["image_path"],use_container_width=True)
        with details:
            st.markdown(f'<article class="rec-copy"><span>{item["brand"]} · {item["style"]}</span><h2>{item["title"]}</h2><p>{item["description"]}</p><div class="reason"><b>WHY IT WORKS</b><br>{item["explanation"]}</div><small>{item["occasion"]} &nbsp; · &nbsp; {item["season"]} &nbsp; · &nbsp; {item["colors"]}</small></article>',unsafe_allow_html=True)
        with action:
            st.markdown(f'<div class="match"><b>{item["score"]:.0f}</b><span>% MATCH</span></div><div class="price">${item["price"]:.0f}</div>',unsafe_allow_html=True)
            if st.button("♡ Save",key=f'save_{item["id"]}',use_container_width=True): db.add_favorite(item); st.toast("Saved to wardrobe")
            st.link_button("Shop ↗",item["shopping_url"],use_container_width=True)
            with st.popover("Rate this"):
                if st.button("Helpful",key=f'yes_{index}'): db.add_feedback(int(item["id"]),True); st.toast("Thank you")
                if st.button("Not for me",key=f'no_{index}'): db.add_feedback(int(item["id"]),False); st.toast("Feedback saved")
        st.divider()