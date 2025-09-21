from newsapi import NewsApiClient
import sqlite3
import time
from datetime import datetime
from config import NEWS_API_KEY, HAZARD_KEYWORDS, INDIAN_COASTAL_CITIES
from database import DB_FILE

def analyze_and_store(article, source):
    full_text = f"{article['title']}. {article['description'] or ''}"
    lower_text = full_text.lower()
    for hazard_type, keywords in HAZARD_KEYWORDS.items():
        if any(keyword in lower_text for keyword in keywords):
            for city in INDIAN_COASTAL_CITIES:
                if city in lower_text:
                    try:
                        conn = sqlite3.connect(DB_FILE)
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO staged_events (source, hazard_type, location, text, url) VALUES (?, ?, ?, ?, ?)",
                            (source, hazard_type, city.capitalize(), full_text, article['url'])
                        )
                        conn.commit()
                        conn.close()
                        print(f"[News Collector] Staged event: '{hazard_type}' in '{city.capitalize()}' from '{source}'")
                    except sqlite3.IntegrityError:
                        pass # Ignore if URL is already in DB
                    return

def run_news_collector():
    if NEWS_API_KEY == "YOUR_NEWSAPI_KEY_HERE":
        print("[News Collector] WARNING: News API key not configured. This collector will be idle.")
        return # Exit the function if no key is provided
        
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    print("[News Collector] Starting polling cycles...")
    while True:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [News Collector] Fetching latest articles...")
        
        # Creates a big search query string like "tsunami OR flooding OR..."
        query = " OR ".join(sum(HAZARD_KEYWORDS.values(), []))
        
        try:
            articles = newsapi.get_everything(
                q=query, 
                language='en', 
                sort_by='publishedAt', 
                page_size=20, # Get a few recent articles
                domains='timesofindia.indiatimes.com,thehindu.com,indiatoday.in,ndtv.com'
            )
            
            if articles['articles']:
                for article in articles['articles']:
                    analyze_and_store(article, article['source']['name'])
            else:
                print(f"[{timestamp}] [News Collector] No relevant articles found in this cycle.")

        except Exception as e:
            print(f"[{timestamp}] [News Collector] ERROR fetching news: {e}")
        
        # --- NEW: Clearer status message ---
        print(f"[{timestamp}] [News Collector] Cycle complete. Waiting 15 minutes for the next poll.")
        time.sleep(900) # Wait for 15 minutes (900 seconds)