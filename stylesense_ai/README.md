 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/stylesense_ai/README.md b/stylesense_ai/README.md
index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..5393d567ed1c53be4a40a2b037b7d3cecd7a8269 100644
--- a/stylesense_ai/README.md
+++ b/stylesense_ai/README.md
@@ -0,0 +1,119 @@
+# StyleSense AI
+
+StyleSense AI is a production-oriented, local-first fashion recommendation dashboard built entirely in Python. It combines visual color and category analysis, deterministic image embeddings, content-based recommendation, weighted preference scoring, a persistent wardrobe, feedback, and interactive style analytics in a premium Streamlit interface.
+
+## Features
+
+- Premium responsive UI with dark gradients, glassmorphism, animated controls, and sidebar navigation
+- Validated JPG, JPEG, and PNG upload workflow with local image storage
+- Dominant clothing-color extraction using K-Means and OpenCV
+- Lightweight 112-dimensional HSV and edge image embeddings
+- Editable clothing category and palette analysis
+- Content-based recommendation with cosine similarity and transparent weighted scores
+- Personalization for occasion, style, budget, colors, season, collection, and brands
+- Five ranked recommendation cards with prices, match badges, explanations, saving, feedback, and shopping links
+- SQLite persistence for preferences, recommendations, analyses, favorites, and feedback
+- Wardrobe management and Plotly-powered style analytics
+
+## Requirements
+
+- Python 3.11 or newer
+- Packages listed in `requirements.txt`
+
+## Installation
+
+```bash
+git clone <repository-url>
+cd FashionProject/stylesense_ai
+python -m venv .venv
+source .venv/bin/activate  # Windows: .venv\Scripts\activate
+python -m pip install --upgrade pip
+pip install -r requirements.txt
+```
+
+## Run
+
+```bash
+cd stylesense_ai
+streamlit run app.py
+```
+
+Streamlit opens the application at `http://localhost:8501`. The SQLite schema and upload directory are created automatically on first run.
+
+## Tests
+
+```bash
+cd stylesense_ai
+pytest -q
+```
+
+## Recommendation scoring
+
+| Signal | Weight |
+| --- | ---: |
+| Style | 30% |
+| Occasion | 25% |
+| Color compatibility | 20% |
+| Budget fit | 15% |
+| Season | 10% |
+
+Popularity provides a small tie-breaking boost. When a photo analysis is available, its visual embedding can add a bounded similarity boost. Every result includes its component score breakdown and a plain-language reason.
+
+## Project structure
+
+```text
+stylesense_ai/
+├── app.py
+├── requirements.txt
+├── README.md
+├── assets/
+│   ├── style.css
+│   └── logo.png
+├── data/
+│   ├── outfits.csv
+│   └── sample_images/
+├── database/
+│   ├── db_manager.py
+│   └── stylesense.db
+├── models/
+│   ├── recommender.py
+│   ├── image_embedding.py
+│   └── color_analysis.py
+├── services/
+│   ├── image_service.py
+│   ├── recommendation_service.py
+│   └── scoring_service.py
+├── pages/
+│   ├── home.py
+│   ├── upload_photo.py
+│   ├── recommendations.py
+│   ├── wardrobe.py
+│   └── analytics.py
+├── utils/
+│   ├── constants.py
+│   └── helpers.py
+└── tests/
+    ├── test_recommender.py
+    └── test_image_service.py
+```
+
+## Screenshots
+
+Run the app and capture the Home, Photo Analysis, Recommendations, Wardrobe, and Analytics views. The responsive interface is optimized for desktop dashboards and compact browser widths.
+
+## Privacy and data
+
+Uploaded photos remain in `data/uploads/`. Application records are stored locally in `database/stylesense.db`. Do not commit personal uploads or production databases. Shopping URLs in the included demonstration catalog are placeholders and should be replaced with approved retailer deep links before deployment.
+
+## Production deployment
+
+Use a persistent volume for `data/uploads/` and `database/`, terminate TLS at the platform edge, and place authentication in front of the application for multi-user use. For concurrent multi-user deployments, migrate the SQLAlchemy connection URL to a managed PostgreSQL database and associate records with authenticated user IDs.
+
+## Future work
+
+- Fine-tuned fashion vision encoders and garment segmentation
+- Retailer inventory and live-price integrations
+- Multi-user authentication and encrypted object storage
+- Virtual try-on with explicit consent controls
+- Collaborative filtering based on opt-in interaction history
+- Accessibility audits, localization, and native mobile clients
 
EOF
)