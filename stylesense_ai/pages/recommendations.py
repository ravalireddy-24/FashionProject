"""Recommendations feature hub."""

import streamlit as st
from database.db_manager import DatabaseManager

FEATURES = (
    ("✦", "Smart Outfit<br>Recommendations", "AI curates outfits just for you", "violet"),
    ("▣", "Virtual Try-On", "See how outfits look on you instantly", "pink"),
    ("♧", "Style Insights", "Get tips to improve your style game", "violet"),
    ("▥", "Wardrobe Manager", "Organize, mix & match your wardrobe", "pink"),
    ("♙", "Shopping Assistant", "Find similar looks from top brands", "violet"),
    ("♡", "Save & Share", "Save your favorite looks and share with ease", "pink"),
)


def _feature_card(icon: str, title: str, copy: str, accent: str) -> str:
    return (
        f'<article class="recommendation-card {accent}">'
        f'<div class="recommendation-icon">{icon}</div>'
        f'<h2>{title}</h2><p>{copy}</p>'
        '<span class="recommendation-link">Explore <b>⟶</b></span>'
        '</article>'
    )

def render(db: DatabaseManager) -> None:
    """Render the recommendation tools landing page."""
    del db  # Kept in the page signature for consistency with the app router.

    st.markdown('<div class="recommendations-page"></div>', unsafe_allow_html=True)

    search, actions = st.columns([5.5, 1.45], vertical_alignment="center")
    with search:
        st.text_input(
            "Search",
            placeholder="Search looks, categories or brands...",
            label_visibility="collapsed",
            key="recommendation_search",
        )
    with actions:
        st.markdown(
            '<div class="recommendation-user"><span class="bell">♧<i></i></span>'
            '<span class="user-avatar">SS</span><span><b>Style Explorer</b>'
            '<small>Personal account</small></span><em>⌄</em></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<section class="recommendation-hero"><div><h1>Recommendations</h1>'
        '<p>Explore personalized styling features crafted for you.</p></div>'
        '<div class="outfit-display"><span class="spark one">✦</span>'
        '<div class="outfit-tile side">♜<small>JACKET</small></div>'
        '<div class="outfit-tile main">♛<b>♡</b><small>YOUR MATCH</small></div>'
        '<div class="outfit-tile side">♟<small>TOP</small></div>'
        '<span class="spark two">✦</span></div></section>',
        unsafe_allow_html=True,
    )

    cards = "".join(_feature_card(*feature) for feature in FEATURES)
    st.markdown(f'<section class="recommendation-grid">{cards}</section>', unsafe_allow_html=True)

    st.markdown(
        '<aside class="learning-banner"><span>✦</span><div><b>Your AI Stylist is always learning</b>'
        '<p>The more you explore, the better your recommendations become.</p></div>'
        '<a href="#recommendation-tools">Explore Looks</a></aside>',
        unsafe_allow_html=True,
    )