import streamlit as st

from utils.ui import metric_row
def _go_to(page: str) -> None:
    st.session_state.page = page
    st.rerun()

def render() -> None:
    st.markdown(
        """
        <nav class="landing-nav">
            <div class="landing-brand">
                <span class="landing-logo">♟</span>
                <span><b>StyleSense</b><small>Dress Better. Instantly.</small></span>
            </div>
            <div class="landing-links">
                <a href="#top">Home</a><a href="#how-it-works">How It Works</a>
                <a href="#features">Features</a><a href="#style-guide">Style Guide</a>
                <a href="#pricing">Pricing</a><a href="#about">About</a>
            </div>
            <div class="landing-actions"><button class="icon-button">☼</button><button>Sign in</button></div>
        </nav>
        <div id="top"></div>
        """,
        unsafe_allow_html=True,
    )

    copy, preview = st.columns([0.9, 1.1], gap="large", vertical_alignment="center")
    with copy:
        st.markdown(
            """
      <section class="reference-hero-copy">
                <h1>Upload. Analyze.<br>Get Outfits That<br><span>Truly Suit You.</span></h1>
                <p>Our AI understands your body, style, preferences and occasions to create perfect looks for you.</p>
                <div class="benefit-grid">
                    <div><i>✿</i><span><b>AI Body Analysis</b><small>Advanced Computer Vision</small></span></div>
                    <div><i>♡</i><span><b>Style Match Score</b><small>Personalized For You</small></span></div>
                    <div><i>♧</i><span><b>Occasion Based</b><small>Perfect for Every Moment</small></span></div>
                    <div><i>▣</i><span><b>Save &amp; Organize</b><small>Your Looks &amp; Favorites</small></span></div>
                </div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="upload-label">✦ &nbsp; Upload Your Photo <small>JPG, PNG or HEIC (Max 20MB)</small></div>',
            unsafe_allow_html=True)
        if st.button("Upload Photo", type="primary", key="home_upload"):
            _go_to("Upload")

    with preview:
        st.markdown(
            """
                   <div class="fashion-preview" role="img" aria-label="AI outfit analysis preview">
                <div class="photo-scene"><div class="person-silhouette"><span></span></div></div>
                <div class="analysis-score"><b>96%</b><small>Style Match</small></div>
                <div class="analysis-pills">
                    <div><i>♧</i><span>Body Shape<b>Hourglass</b></span></div>
                    <div><i>●</i><span>Skin Tone<b>Warm Beige</b></span></div>
                    <div><i>●●●</i><span>Color Palette<b>Warm Autumn</b></span></div>
                    <div><i>↕</i><span>Height<b>5'5&quot;</b></span></div>
                    <div><i>▱</i><span>Best Fit<b>Regular Fit</b></span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
  <section class="feature-strip" id="features">
            <h2>Powerful Features to Elevate Your Style <span>✦</span></h2>
            <div class="feature-strip-grid">
                <article><i>♟</i><b>Smart Outfit<br>Recommendations</b><small>AI curates outfits just for you</small></article>
                <article><i>✣</i><b>Virtual Try-On</b><small>See how outfits look on you instantly</small></article>
                <article><i>✥</i><b>Style Insights</b><small>Get tips to improve your style game</small></article>
                <article><i>▣</i><b>Wardrobe Manager</b><small>Organize, mix &amp; match your wardrobe</small></article>
                <article><i>🛒</i><b>Shopping Assistant</b><small>Find similar looks from top brands</small></article>
                <article><i>♡</i><b>Save &amp; Share</b><small>Save favorites and share with friends</small></article>
            </div>
        </section>
        <section class="how-strip" id="how-it-works">
            <h2>How It Works</h2>
            <div class="steps-grid">
                <article><i>♙</i><b>1. Upload Photo</b><small>Upload a clear full-body photo of yourself</small></article>
                <article><i>✣</i><b>2. AI Analysis</b><small>Our AI analyzes your body, skin tone &amp; preferences</small></article>
                <article><i>♙</i><b>3. Get Outfits</b><small>Receive personalized outfit recommendations</small></article>
                <article><i>♧</i><b>4. Save &amp; Shop</b><small>Save your favorite looks and shop directly</small></article>
            </div>
        </section>
        <div class="landing-stats"><div><b>1M+</b><small>Happy Users</small></div><div><b>10M+</b><small>Outfits Generated</small></div><div><b>200+</b><small>Top Brands</small></div><div><b>98%</b><small>User Satisfaction</small></div></div>
        """,
        unsafe_allow_html=True,
    )

