import sqlite3

DB_FILE = "events.db"

def create_database():
    """Creates the necessary database tables if they don't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Table for all raw, unverified events from collectors
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staged_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        hazard_type TEXT NOT NULL,
        location TEXT NOT NULL,
        text TEXT,
        url TEXT UNIQUE
    )
    """)

    # Table for high-confidence, confirmed alerts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS confirmed_alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        hazard_type TEXT NOT NULL,
        location TEXT NOT NULL,
        confidence_score INTEGER,
        contributing_sources TEXT
    )
    """)
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    create_database()