import praw
import sqlite3
import time
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, HAZARD_KEYWORDS, INDIAN_COASTAL_CITIES
from database import DB_FILE

def analyze_and_store(text, url, source, subreddit):
    lower_text = text.lower()
    for hazard_type, keywords in HAZARD_KEYWORDS.items():
        if any(keyword in lower_text for keyword in keywords):
            for city in INDIAN_COASTAL_CITIES:
                if city in lower_text:
                    try:
                        conn = sqlite3.connect(DB_FILE)
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO staged_events (source, hazard_type, location, text, url) VALUES (?, ?, ?, ?, ?)",
                            (f"{source}/{subreddit}", hazard_type, city.capitalize(), text, url)
                        )
                        conn.commit()
                        conn.close()
                        print(f"[Reddit Collector] Staged event: '{hazard_type}' in '{city.capitalize()}'")
                    except sqlite3.IntegrityError:
                        pass # Ignore if URL is already in DB
                    return

def run_reddit_collector():
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)
    subreddit = reddit.subreddit("india+mumbai+chennai+kolkata+Goa")
    print("[Reddit Collector] Listening for new posts...")
    for submission in subreddit.stream.submissions(skip_existing=True):
        full_text = f"{submission.title}. {submission.selftext}"
        analyze_and_store(full_text, submission.shortlink, "Reddit", submission.subreddit.display_name)