import sqlite3
import time
from datetime import datetime
from database import DB_FILE

# --- Correlation Rules ---
CONFIRMATION_THRESHOLD = 2  # How many unique sources are needed to confirm an event
TIME_WINDOW_MINUTES = 60    # How far back to look for related events

def run_correlation_engine():
    print("[Correlation Engine] Starting analysis cycles...")
    while True:
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()

            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] [Correlation Engine] Checking for correlated events...")

            # Get recent staged events
            cursor.execute(f"SELECT hazard_type, location, source FROM staged_events WHERE timestamp >= datetime('now', '-{TIME_WINDOW_MINUTES} minutes')")
            recent_events = cursor.fetchall()

            # Group events by hazard and location
            event_groups = {}
            if recent_events:
                for hazard, location, source in recent_events:
                    key = (hazard, location)
                    if key not in event_groups:
                        event_groups[key] = set()
                    event_groups[key].add(source.split('/')[0])

                # Check if any group meets the confirmation threshold
                for (hazard, location), sources in event_groups.items():
                    if len(sources) >= CONFIRMATION_THRESHOLD:
                        # This is a confirmed event!
                        try:
                            cursor.execute(
                                "INSERT INTO confirmed_alerts (hazard_type, location, confidence_score, contributing_sources) VALUES (?, ?, ?, ?)",
                                (hazard, location, len(sources), ", ".join(sources))
                            )
                            conn.commit()
                            print(f"\n*** [Correlation Engine] CONFIRMED ALERT: '{hazard}' in '{location}' (Sources: {', '.join(sources)}) ***\n")
                            
                            # Clean up staged events that contributed to this alert
                            cursor.execute("DELETE FROM staged_events WHERE hazard_type = ? AND location = ?", (hazard, location))
                            conn.commit()

                        except sqlite3.IntegrityError:
                            pass
            else:
                # --- NEW: Explicitly state when no events are found ---
                print(f"[{timestamp}] [Correlation Engine] No new staged events found in the last {TIME_WINDOW_MINUTES} minutes.")

            conn.close()
        except Exception as e:
            print(f"[Correlation Engine] ERROR: {e}")

        # Run the correlation check every minute
        time.sleep(60)