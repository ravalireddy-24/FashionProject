import streamlit as st
from utils.ui import metric_row
def render() -> None:
left, right = st.columns([1.08, 0.92], gap="large", vertical_alignment="center")
    with left:
        st.markdown(
            '<section class="hero-copy"><div class="eyebrow">✦ YOUR PERSONAL AI STYLIST</div>'
            '<h1>Style that feels <span>uniquely you.</span></h1>'
            '<p>Upload a photo and let StyleSense AI curate outfits around your palette, '
            'preferences, occasion, and budget.</p></section>',
            unsafe_allow_html=True,
        )
        primary, secondary = st.columns(2, gap="small")
        if primary.button("Upload a photo  →", type="primary", use_container_width=True):
            st.session_state.page = "Upload"
            st.rerun()
        if secondary.button("Explore recommendations", use_container_width=True):
            st.session_state.page = "Recommendations"
            st.rerun()
        metric_row([("10K+", "looks curated"), ("4.9/5", "stylist rating"), ("100%", "private")])
    with right:
        st.markdown(
            '<div class="visual-card" role="img" aria-label="Style recommendation preview, '
            '96 percent match for a business casual warm neutral look">'
            '<div class="preview-top"><span>STYLE PREVIEW</span><b>01 / 05</b></div>'
            '<div class="orb"></div><div class="model-mark">S</div>'
            '<div class="score-ring"><strong>96%</strong><small>STYLE MATCH</small></div>'
            '<div class="floating-tag one">✦ Business casual</div>'
            '<div class="floating-tag two">● Warm neutral palette</div>'
            '<div class="preview-caption"><span>CURATED FOR YOU</span>'
            '<strong>Soft structure, confident detail.</strong></div></div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-heading"><span>WHY STYLESENSE</span>'
            '<h2>Great style, made effortless.</h2></div>',
            unsafe_allow_html=True,
        )
        cols = st.columns(4, gap="medium")
        features = [
            ("✦", "AI Style Analysis", "Understands colors, silhouettes, and the details that make your style yours."),
            ("◈", "Smart Matching", "Ranks every look using transparent, preference-aware scoring."),
            ("♡", "Digital Wardrobe", "Save favorites in one beautiful, organized collection."),
            ("↗", "Shop Confidently", "Explore curated items that suit your style and your budget."),
        ]
        for col, (icon, title, copy) in zip(cols, features):
            col.markdown(
                f'<article class="glass feature"><i>{icon}</i><h3>{title}</h3><p>{copy}</p></article>',
                unsafe_allow_html=True,
            )
        st.markdown(
            '<div class="testimonial glass">“StyleSense made getting dressed for work feel exciting again.” '
            '<span>— MAYA, PRODUCT DESIGNER</span></div><footer><b>StyleSense AI</b>'
            '<span>Intelligent style. Designed around you.</span><small>© 2026 StyleSense</small></footer>',
            unsafe_allow_html=True,
        )