import sqlite3

DB_FILE = "events.db"

def create_database():
    """Creates and updates the database tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

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

    # --- NEW: Add columns for vision analysis ---
    try:
        cursor.execute("ALTER TABLE staged_events ADD COLUMN vision_hazard_detected BOOLEAN")
        cursor.execute("ALTER TABLE staged_events ADD COLUMN vision_description TEXT")
    except sqlite3.OperationalError:
        pass # Columns already exist, ignore the error

    # ... (rest of the file is the same) ...
    conn.commit()
    conn.close()
    print("Database initialized successfully.")
