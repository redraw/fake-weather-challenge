from app.settings.base import *

WEATHER_API_URL = os.getenv("WEATHER_API_URL", "http://localhost:5000")
STATIC_ROOT = os.path.join(BASE_DIR, "static")
