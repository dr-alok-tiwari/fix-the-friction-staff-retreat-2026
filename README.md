# Fix the Friction | Staff Retreat 2026

A local Streamlit website for presenting Staff Retreat 2026 Sub-theme 01: **Fix the Friction** in a constructive, non-blaming, solution-oriented format.

## Features

- Interactive issue explorer
- Visual dashboard with Plotly charts
- Impact × feasibility prioritization matrix
- Top 3 bottlenecks synthesis
- 5-Whys root-cause cards
- Solution gallery
- 30–60–90 day roadmap
- KPI tracker
- Reflection wall using Streamlit session state
- Downloadable Markdown and CSV reports
- Presentation mode for projector display

## Local Setup

### 1. Create a project folder

```bash
mkdir fix_the_friction_streamlit
cd fix_the_friction_streamlit
```

Place `app.py` and `requirements.txt` in this folder.

### 2. Create a virtual environment

Windows PowerShell:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The website will open in your browser, usually at:

```text
http://localhost:8501
```

## Notes

- No API key is required.
- No paid service is required.
- The app stores reflection-wall notes only in the current browser session.
- All issue statements are framed as improvement opportunities rather than complaints.
