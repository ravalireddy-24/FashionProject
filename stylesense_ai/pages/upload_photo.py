import streamlit as st
from PIL import Image
from database.db_manager import DatabaseManager
from services.image_service import ImageService
from utils.constants import SUPPORTED_IMAGE_TYPES

def render(db: DatabaseManager) -> None:
    st.markdown(
        """
        <div class="page-title upload-page-title">
            <span>01 / ANALYZE</span>
            <h1>Discover your visual signature.</h1>
            <p>Add a clear outfit photo. Your image stays local and is used only for this analysis.</p>
        </div>
        <section class="upload-benefits" aria-label="Personalized styling benefits">
            <article>
                <i aria-hidden="true">✿</i>
                <div><b>AI Body Analysis</b><small>Advanced Computer Vision</small></div>
            </article>
            <article>
                <i aria-hidden="true">♡</i>
                <div><b>Style Match Score</b><small>Personalized For You</small></div>
            </article>
            <article>
                <i aria-hidden="true">♧</i>
                <div><b>Occasion Based</b><small>Perfect for Every Moment</small></div>
            </article>
            <article>
                <i aria-hidden="true">▣</i>
                <div><b>Save &amp; Organize</b><small>Your Looks &amp; Favorites</small></div>
            </article>
        </section>
        """,
        unsafe_allow_html=True,
    )
    uploaded=st.file_uploader("Drop an outfit photo here", type=SUPPORTED_IMAGE_TYPES, help="JPG, JPEG or PNG · maximum 20 MB")
    if uploaded:
        service=ImageService()
        try:
            path=service.save(uploaded, uploaded.name); analysis=service.analyze(path)
        except ValueError as exc: st.error(str(exc)); return
        st.session_state.analysis=analysis; st.session_state.upload_path=str(path)
        a,b=st.columns([1,1], gap="large")
        with a: st.image(Image.open(path), use_container_width=True)
        with b:
            st.markdown('<div class="analysis-card"><span class="status">✦ ANALYSIS COMPLETE</span><h2>Your style signals</h2></div>', unsafe_allow_html=True)
            names=[c["name"] for c in analysis["dominant_colors"]]
            category=st.selectbox("Detected category", [analysis["category"], "Dress", "Outerwear", "Top & Bottom", "Accessories"])
            colors=st.multiselect("Detected clothing colors", ["Black","White","Beige","Brown","Gray","Navy","Blue","Green","Red","Pink","Purple","Orange","Yellow"], default=names)
            swatches="".join(f'<span class="swatch" style="background:{c["hex"]}" title="{c["name"]}"></span>' for c in analysis["dominant_colors"])
            st.markdown(f'<div class="palette">{swatches}</div>',unsafe_allow_html=True)
            if st.button("Save analysis & personalize →", type="primary", use_container_width=True):
                analysis["category"] = category;
                analysis["dominant_colors"] = [{"name": x} for x in colors];
                analysis["image_path"] = str(path);
                db.save_analysis(analysis);
                st.session_state.page = "Recommendations";
                st.rerun()