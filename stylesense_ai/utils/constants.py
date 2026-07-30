from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
SAMPLE_DIR = DATA_DIR / "sample_images"
DATABASE_PATH = ROOT_DIR / "database" / "stylesense.db"
OUTFITS_PATH = DATA_DIR / "outfits.csv"
SUPPORTED_IMAGE_TYPES = ("jpg", "jpeg", "png")
OCCASIONS = ["Office", "Wedding", "Casual", "Travel", "Party"]
STYLES = ["Minimal", "Streetwear", "Luxury", "Business Casual", "Sporty", "Elegant"]
SEASONS = ["Spring", "Summer", "Autumn", "Winter", "All Season"]
GENDERS = ["Womenswear", "Menswear", "Gender Neutral"]
WEIGHTS = {"style": 0.30, "occasion": 0.25, "color": 0.20, "budget": 0.15, "season": 0.10}
DEFAULT_PREFERENCES = {"occasion": "Office", "style": "Business Casual", "budget": 180.0, "preferred_colors": ["Beige", "Black", "White"], "season": "All Season", "gender": "Gender Neutral", "favorite_brands": ["Aster & Row"]}