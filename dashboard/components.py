"""Reusable Streamlit UI components."""

from __future__ import annotations

from collections.abc import Mapping

import pandas as pd
import streamlit as st


def render_header(title: str, subtitle: str) -> None:
    """Render the dashboard title block."""
    st.title(title)
    st.caption(subtitle)


def render_status_panel(items: Mapping[str, str]) -> None:
    """Render a simple list of analysis modules and their purpose."""
    for name, description in items.items():
        st.markdown(f"**{name}**: {description}")


def render_dataset_preview(frame: pd.DataFrame) -> None:
    """Render a compact preview of loaded datasets."""
    st.dataframe(frame, use_container_width=True, hide_index=True)
