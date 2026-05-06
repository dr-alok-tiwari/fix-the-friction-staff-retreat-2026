"""
Mobile responsiveness patch for the Streamlit app.

Python automatically imports `sitecustomize.py` from the project root when the
app starts. This lets us add a safe, non-invasive mobile layer without rewriting
`app.py`.
"""


def _install_streamlit_mobile_patch():
    try:
        import streamlit as st
    except Exception:
        return

    if getattr(st, "_ftf_mobile_patch_installed", False):
        return

    original_set_page_config = st.set_page_config
    original_markdown = st.markdown

    mobile_css = """
    <style>
    /* ============================================================
       Mobile-first responsive layer for Fix the Friction app
       ============================================================ */

    .block-container {
        max-width: 1280px;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    html, body, [class*="css"] {
        -webkit-text-size-adjust: 100%;
        text-size-adjust: 100%;
    }

    p, li, div, span, label {
        overflow-wrap: anywhere;
        word-break: normal;
    }

    .stButton > button,
    .stDownloadButton > button {
        width: 100%;
        min-height: 44px;
        border-radius: 12px;
        font-weight: 700;
        white-space: normal;
    }

    [data-testid="stDataFrame"],
    [data-testid="stTable"],
    [data-testid="stVegaLiteChart"],
    [data-testid="stPlotlyChart"] {
        width: 100% !important;
        overflow-x: auto !important;
    }

    [data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid rgba(18, 53, 91, 0.08);
        border-radius: 16px;
        padding: 0.85rem;
        box-shadow: 0 8px 20px rgba(18, 53, 91, 0.07);
    }

    div[data-testid="stTabs"] button {
        white-space: nowrap;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(18, 53, 91, 0.08);
    }

    @media screen and (max-width: 900px) {
        .block-container {
            padding-top: 0.75rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-bottom: 2rem !important;
        }

        .hero {
            border-radius: 20px !important;
            padding: 1.25rem 1rem !important;
            box-shadow: 0 12px 28px rgba(18, 53, 91, 0.16) !important;
        }

        .hero:after {
            width: 150px !important;
            height: 150px !important;
            right: -60px !important;
            top: -55px !important;
        }

        .hero h1 {
            font-size: 1.85rem !important;
            line-height: 1.12 !important;
            letter-spacing: -0.3px !important;
        }

        .hero p {
            font-size: 0.96rem !important;
            line-height: 1.45 !important;
        }

        .mini-badge,
        .badge {
            display: inline-flex !important;
            align-items: center;
            max-width: 100%;
            margin-bottom: 0.35rem !important;
            font-size: 0.76rem !important;
            line-height: 1.25 !important;
        }

        .section-title {
            font-size: 1.35rem !important;
            line-height: 1.25 !important;
        }

        .section-subtitle {
            font-size: 0.94rem !important;
            line-height: 1.45 !important;
        }

        .card,
        .soft-card,
        .metric-card,
        .progress-card,
        .sticky {
            border-radius: 16px !important;
            padding: 0.9rem !important;
            min-height: unset !important;
            margin-bottom: 0.85rem !important;
        }

        .big-number {
            font-size: 1.55rem !important;
        }

        /* Force Streamlit columns into a readable single-column stack. */
        div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: column !important;
            gap: 0.75rem !important;
        }

        div[data-testid="stColumn"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }

        /* Better mobile spacing for expanders, inputs, and text areas. */
        .element-container {
            margin-bottom: 0.7rem !important;
        }

        textarea {
            min-height: 120px !important;
        }

        [data-testid="stExpander"] details {
            border-radius: 14px !important;
        }

        /* Sidebar behaves like a mobile drawer. */
        section[data-testid="stSidebar"] {
            width: 86vw !important;
            max-width: 360px !important;
        }

        /* Keep tables and charts usable instead of compressed. */
        [data-testid="stDataFrame"] > div,
        [data-testid="stTable"] > div,
        [data-testid="stPlotlyChart"] > div {
            overflow-x: auto !important;
        }
    }

    @media screen and (max-width: 520px) {
        .block-container {
            padding-left: 0.7rem !important;
            padding-right: 0.7rem !important;
        }

        h1, .hero h1 {
            font-size: 1.55rem !important;
        }

        h2 {
            font-size: 1.25rem !important;
        }

        h3 {
            font-size: 1.08rem !important;
        }

        p, li, label, div {
            font-size: 0.93rem;
        }

        .stButton > button,
        .stDownloadButton > button {
            font-size: 0.92rem !important;
            padding: 0.55rem 0.7rem !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.35rem !important;
        }

        [data-testid="stMetricLabel"] {
            font-size: 0.76rem !important;
        }
    }
    </style>
    """

    def patched_set_page_config(*args, **kwargs):
        kwargs["initial_sidebar_state"] = "collapsed"
        result = original_set_page_config(*args, **kwargs)
        try:
            original_markdown(mobile_css, unsafe_allow_html=True)
        except Exception:
            pass
        return result

    st.set_page_config = patched_set_page_config
    st._ftf_mobile_patch_installed = True


_install_streamlit_mobile_patch()
