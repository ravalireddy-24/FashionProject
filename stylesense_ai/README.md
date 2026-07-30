# StyleSense AI

StyleSense AI is a local-first fashion recommendation dashboard built with Streamlit. It combines photo color analysis, preference-aware outfit ranking, a persistent wardrobe, feedback, and interactive analytics in a responsive dark interface.

## Features

- Responsive premium dashboard and custom sidebar navigation
- Validated JPG, JPEG, and PNG photo analysis
- Color extraction and deterministic visual embeddings
- Preference and budget-aware recommendations
- SQLite-backed wardrobe, feedback, and analytics

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r stylesense_ai/requirements.txt
```

## Run

From the repository root:

```bash
streamlit run app.py
```

## Tests

```bash
pytest -q stylesense_ai/tests/test_recommender.py
```

Uploaded images remain local in `stylesense_ai/data/uploads/`, and application data is stored in `stylesense_ai/database/stylesense.db`.