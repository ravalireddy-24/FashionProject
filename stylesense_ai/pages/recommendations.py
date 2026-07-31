"""Recommendations feature hub."""

from html import escape
import streamlit as st
from database.db_manager import DatabaseManager

FEATURES = (
    ("✦", "Smart Outfit Recommendations", "AI-curated combinations shaped around your palette and personal style.", "violet", "Upload"),
    ("▣", "Virtual Try-On", "Preview complete looks against your photo before deciding what to wear.", "pink", "Upload"),
    ("♧", "Style Insights", "Understand why every color, silhouette, and pairing works for you.", "violet", "Analytics"),
    ("▥", "Wardrobe Manager", "Organize your pieces and uncover new combinations from what you own.", "pink", "Wardrobe"),
    ("♙", "Shopping Assistant", "Discover pieces that complement your wardrobe instead of duplicating it.", "violet", "Recommendations"),
    ("♡", "Save & Share", "Keep the looks you love close and share inspiration with confidence.", "pink", "Wardrobe"),
)


def _feature_card(icon: str, title: str, copy: str, accent: str, page: str) -> str:
    """Build a keyboard-accessible feature link for the recommendation grid."""
    return (
        f'<a class="recommendation-card {accent}" href="?page={escape(page)}" target="_self">'
        f'<div class="recommendation-icon" aria-hidden="true">{icon}</div>'
        f'<h2>{escape(title)}</h2><p>{escape(copy)}</p>'
        '<span class="recommendation-link">Explore <b aria-hidden="true">↗</b></span>'
        '</a>'
    )

def render(db: DatabaseManager) -> None:
    """Render the recommendation tools landing page."""
    del db  # Kept in the page signature for consistency with the app router.

    st.markdown(
        '<div class="recommendations-page"></div>'
        '<header class="recommendations-nav">'
        '<a class="recommendations-brand" href="?page=Home" target="_self" aria-label="StyleSense home">'
        '<span>✦</span><div><b>StyleSense</b><small>AI STYLE STUDIO</small></div></a>'
        '<nav aria-label="Primary navigation">'
        '<a href="?page=Home" target="_self">Home</a>'
        '<a href="?page=Upload" target="_self">Analyze</a>'
        '<a class="active" href="?page=Recommendations" target="_self">Recommendations</a>'
        '<a href="?page=Wardrobe" target="_self">Wardrobe</a>'
        '</nav>'
        '<a class="nav-cta" href="?page=Upload" target="_self">Try your look <span>↗</span></a>'
        '</header>',
        unsafe_allow_html=True,
    )
    hero_copy, preview = st.columns([1.08, 1], gap="large", vertical_alignment="center")
    with hero_copy:
        st.markdown(
            '<section class="recommendations-copy">'
            '<span class="recommendations-eyebrow"><i>✦</i> YOUR PERSONAL AI STYLIST</span>'
            '<h1>Style that feels<br><em>distinctly yours.</em></h1>'
            '<p>Turn your wardrobe, features, and preferences into considered outfit '
            'recommendations—made for your real life, not a generic trend report.</p>'
            '<div class="recommendations-actions">'
            '<a class="primary" href="?page=Upload" target="_self">Get my recommendations <span>↗</span></a>'
            '<a class="secondary" href="#recommendation-tools">Explore features</a>'
            '</div>'
            '<div class="recommendations-proof"><div><b>94%</b><small>AVERAGE STYLE MATCH</small></div>'
            '<div><b>6</b><small>PERSONAL SIGNALS</small></div>'
            '<div><b>∞</b><small>WAYS TO WEAR</small></div></div>'
            '</section>',
            unsafe_allow_html=True,
        )
    with preview:
        st.markdown(
            '<section class="recommendations-preview" aria-label="AI outfit recommendation preview">'
            '<div class="preview-glow"></div><div class="preview-frame">'
            '<div class="preview-meta"><span>CURATED FOR YOU</span><b>LOOK 01 / 04</b></div>'
            '<div class="preview-model"><span class="model-head"></span><span class="model-body"></span></div>'
            '<span class="preview-spark spark-a">✦</span><span class="preview-spark spark-b">✦</span>'
            '<div class="preview-style"><small>TODAY’S DIRECTION</small><b>Soft structure</b><span>Warm neutrals · Evening</span></div>'
            '</div><div class="recommendation-score"><b>94</b><small>STYLE<br>MATCH</small></div>'
            '<div class="preview-card palette-card"><i>◐</i><span><small>YOUR PALETTE</small><b>Warm Autumn</b></span>'
            '<em><u></u><u></u><u></u></em></div>'
            '<div class="preview-card occasion-card"><i>◇</i><span><small>PERFECT FOR</small><b>Gallery evening</b></span></div>'
            '<div class="preview-card reason-card"><span>WHY IT WORKS</span><p>Clean lines balance the soft palette while the accent adds depth.</p></div>'
            '</section>',
            unsafe_allow_html=True,
        )

        cards = "".join(_feature_card(*feature) for feature in FEATURES)

    st.markdown(
        '<section class="recommendation-section" id="recommendation-tools">'
        '<div class="recommendation-heading"><span>ONE STUDIO. EVERY LOOK.</span>'
        '<h2>Intelligence, tailored to you.</h2><p>From first analysis to final outfit, every tool learns your taste.</p></div>'
        f'<div class="recommendation-grid">{cards}</div></section>',
        unsafe_allow_html=True,
    )


    st.markdown(
        '<aside class="learning-banner"><span>✦</span><div><b>Your AI stylist keeps getting better.</b>'
        '<p>Every saved look and wardrobe update makes your next recommendation more personal.</p></div>'
        '<a href="?page=Upload" target="_self">Build my style profile <b>↗</b></a></aside>',
        unsafe_allow_html=True,
    )