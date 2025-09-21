# --- Central Configuration File ---

# Reddit API Credentials
REDDIT_CLIENT_ID = "wsADFqZw0UXO0sea14V0dg"
REDDIT_CLIENT_SECRET = "mi7uOtYnt_9uZP6DuypAk2qN_myZLA"
REDDIT_USER_AGENT = "ocean-hazard-monitor/0.1 by Beautiful-Tough-4384"

# NewsAPI.org Credentials
NEWS_API_KEY = "04637f1c3f96493896b30b3002f2d3c1"

# Gemini API Credentials
GEMINI_API_KEY = "AIzaSyDWb5A-os8KwsTfvhmx-Vk3hvwcHCWxCAA"

# --- NLP Keywords (Shared across all collectors) ---
HAZARD_KEYWORDS = {
    "tsunami": ["tsunami", "tidal wave", "harbor wave", "sea receding"],
    "storm_surge": ["storm surge", "coastal flood", "high tide", "rising sea"],
    "high_waves": ["high waves", "rough seas", "big waves", "dangerous waves"],
    "flooding": ["flooding", "water logging", "inundation", "submerged", "water entering"]
}

INDIAN_COASTAL_CITIES = [
    "mumbai", "chennai", "kolkata", "kochi", "visakhapatnam", "vizag", "goa",
    "puducherry", "pondicherry", "mangaluru", "kanyakumari", "puri", "digha"
]
