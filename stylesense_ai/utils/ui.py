"""Reusable presentation helpers for a consistent Streamlit interface."""

from html import escape

import streamlit as st


NAV_ITEMS = (
    ("Home", "⌂"),
    ("Upload", "⊕"),
    ("Recommendations", "✦"),
    ("Wardrobe", "♡"),
    ("Analytics", "▥"),
)


def page_header(eyebrow: str, title: str, description: str) -> None:
    st.markdown(
        f'<header class="page-title"><span>{escape(eyebrow)}</span>'
        f'<h1>{escape(title)}</h1><p>{escape(description)}</p></header>',
        unsafe_allow_html=True,
    )


def badge(text: str, class_name: str = "badge") -> str:
    return f'<span class="{class_name}">{escape(text)}</span>'


def metric_row(items: list[tuple[str, str]]) -> None:
    content = "".join(
        f'<div><strong>{escape(value)}</strong><span>{escape(label)}</span></div>'
        for value, label in items
    )
    st.markdown(f'<div class="trust-metrics">{content}</div>', unsafe_allow_html=True)


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown(
            '<div class="brand"><div class="brand-mark">✦</div>'
            '<div class="brand-name"><b>StyleSense</b><small>Your intelligent wardrobe</small></div>'
            '<span class="brand-ai">AI</span></div>',
            unsafe_allow_html=True,
        )
        st.markdown('<div class="nav-label">YOUR STUDIO</div>', unsafe_allow_html=True)
        for label, icon in NAV_ITEMS:
            active = st.session_state.page == label
            if st.button(
                f"{icon}  {label}",
                key=f"nav_{label}",
                type="primary" if active else "secondary",
                use_container_width=True,
            ):
                st.session_state.page = label
                st.rerun()
        st.markdown(
            '<div class="sidebar-bottom"><div class="side-card">'
            '<span>STYLE PROFILE</span><b>Build your signature look</b>'
            '<p>Upload a photo to unlock palette-aware recommendations.</p>'
            '</div><div class="side-footer"><span class="avatar">SS</span>'
            '<div><b>Style Explorer</b><small>Private profile</small></div></div></div>',
            unsafe_allow_html=True,
        )