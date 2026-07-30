import streamlit as st

def render() -> None:
    st.markdown('<section class="hero"><div class="eyebrow">✦ YOUR PERSONAL AI STYLIST</div><h1>Style that feels<br><span>uniquely you.</span></h1><p>Upload a photo and let StyleSense AI curate outfits around your palette, preferences, occasion, and budget.</p></section>', unsafe_allow_html=True)
    left, right = st.columns([1, 1.1], gap="large")
    with left:
        c1,c2 = st.columns(2)
        if c1.button("Upload a photo  →", type="primary", use_container_width=True): st.session_state.page="Upload"; st.rerun()
        if c2.button("Explore demo", use_container_width=True): st.session_state.page="Recommendations"; st.rerun()
        st.markdown('<div class="trust"><b>10K+</b> looks curated &nbsp; · &nbsp; <b>4.9/5</b> stylist rating</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="visual-card"><div class="orb"></div><div class="score-ring">96%<small>STYLE MATCH</small></div><div class="floating-tag one">✦ Business casual</div><div class="floating-tag two">● Warm neutral palette</div><div class="model-mark">S</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading"><span>WHY STYLESENSE</span><h2>Great style, made effortless.</h2></div>', unsafe_allow_html=True)
    cols=st.columns(4)
    features=[("✦","AI Style Analysis","Understands colors, silhouettes, and the details that make your style yours."),("◈","Smart Matching","Ranks every look using transparent, preference-aware scoring."),("♡","Digital Wardrobe","Save favorites in one beautiful, organized collection."),("↗","Shop Confidently","Explore curated items that suit your style and your budget.")]
    for col,(icon,title,copy) in zip(cols,features): col.markdown(f'<article class="glass feature"><i>{icon}</i><h3>{title}</h3><p>{copy}</p></article>', unsafe_allow_html=True)
    st.markdown('<div class="testimonial glass">“StyleSense made getting dressed for work feel exciting again.” <span>— MAYA, PRODUCT DESIGNER</span></div><footer>StyleSense AI <span>Intelligent style. Designed around you.</span> <small>© 2026 StyleSense</small></footer>', unsafe_allow_html=True)