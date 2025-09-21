import praw
import sqlite3
import time
import requests # For downloading images
import base64   # For encoding images
import json
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, GEMINI_API_KEY, HAZARD_KEYWORDS, INDIAN_COASTAL_CITIES
from database import DB_FILE

# --- NEW: Gemini Vision Analysis Function ---
def analyze_image_with_gemini(image_url: str) -> dict | None:
    """
    Downloads an image, sends it to the Gemini API for analysis, and returns the result.
    """
    if GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        # Silently skip if the key is not configured
        return None

    try:
        # 1. Download the image
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status() # Raise an error for bad status codes
        
        # 2. Encode the image to base64
        image_data = response.content
        base64_image = base64.b64encode(image_data).decode('utf-8')

        # 3. Prepare the request for Gemini API
        gemini_api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key={GEMINI_API_KEY}"
        
        prompt = """
        You are a disaster analyst. Analyze this image from a social media post in a coastal area of India.
        1. Does this image show clear evidence of flooding, high waves, storm surge, or a tsunami?
        2. Briefly describe the key visual evidence in one sentence.
        3. Rate the severity from 1 (low) to 5 (critical).
        
        Return your answer ONLY as a valid JSON object with the keys: "is_hazard", "description", and "severity".
        Example: {"is_hazard": true, "description": "Seawater is flooding a street with cars partially submerged.", "severity": 4}
        """

        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/jpeg", "data": base64_image}}
                ]
            }]
        }

        # 4. Make the API call
        api_response = requests.post(gemini_api_url, json=payload, timeout=30)
        api_response.raise_for_status()
        
        # 5. Parse the response
        result_json = api_response.json()
        # The actual response is nested; we need to extract the JSON string and parse it again.
        content_text = result_json['candidates'][0]['content']['parts'][0]['text']
        vision_result = json.loads(content_text)
        
        print(f"[Gemini Vision] Analysis complete for {image_url}: {vision_result}")
        return vision_result

    except Exception as e:
        print(f"[Gemini Vision] ERROR: Could not analyze image {image_url}. Reason: {e}")
        return None

def run_reddit_collector():
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)
    subreddit = reddit.subreddit("india+mumbai+chennai+kolkata+Goa")
    print("[Reddit Collector] Listening for new posts (with vision capability)...")

    for submission in subreddit.stream.submissions(skip_existing=True):
        full_text = f"{submission.title}. {submission.selftext}"
        lower_text = full_text.lower()
        
        text_hazard_detected = False
        hazard_type = None
        location = None

        # --- Text Analysis (Fast Pass) ---
        for h_type, keywords in HAZARD_KEYWORDS.items():
            if any(keyword in lower_text for keyword in keywords):
                for city in INDIAN_COASTAL_CITIES:
                    if city in lower_text:
                        text_hazard_detected = True
                        hazard_type = h_type
                        location = city.capitalize()
                        break
            if text_hazard_detected:
                break
        
        # --- Vision Analysis (Deep Dive) ---
        vision_result = None
        # Check if the URL is a direct link to an image
        if hasattr(submission, 'url') and submission.url.endswith(('.jpg', '.jpeg', '.png')):
            vision_result = analyze_image_with_gemini(submission.url)
        
        # --- Correlate and Store ---
        # We store an event if EITHER text OR vision detects a hazard
        if text_hazard_detected or (vision_result and vision_result.get("is_hazard")):
            # If vision detected a hazard but text didn't, we need to infer the type and location
            if not text_hazard_detected and vision_result:
                # Simple logic: use the vision description to do a keyword search
                # A more advanced model could have Gemini itself classify the hazard type
                vision_desc_lower = vision_result.get("description", "").lower()
                for h_type, keywords in HAZARD_KEYWORDS.items():
                    if any(keyword in vision_desc_lower for keyword in keywords):
                        hazard_type = h_type
                        break
                # Try to find a location in the post text even if hazard words were absent
                for city in INDIAN_COASTAL_CITIES:
                    if city in lower_text:
                        location = city.capitalize()
                        break

            # Only store if we have identified a hazard and a location
            if hazard_type and location:
                try:
                    conn = sqlite3.connect(DB_FILE)
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO staged_events (source, hazard_type, location, text, url, vision_hazard_detected, vision_description) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (
                            f"Reddit/{submission.subreddit.display_name}",
                            hazard_type,
                            location,
                            full_text,
                            submission.shortlink,
                            vision_result.get("is_hazard") if vision_result else None,
                            vision_result.get("description") if vision_result else None,
                        )
                    )
                    conn.commit()
                    conn.close()
                    print(f"[Collector] Staged multimodal event: '{hazard_type}' in '{location}'")
                except sqlite3.IntegrityError:
                    pass # Ignore duplicates
