import multiprocessing
import time
from datetime import datetime
from database import create_database
from collectors.reddit_collector import run_reddit_collector
from collectors.news_collector import run_news_collector
from engine.correlation import run_correlation_engine

if __name__ == "__main__":
    # 1. Set up the database first
    create_database()

    # 2. Define the processes to run
    # We give each process a clear name for better status reporting
    processes_to_run = {
        "RedditCollector": run_reddit_collector,
        "NewsCollector": run_news_collector,
        "CorrelationEngine": run_correlation_engine,
    }
    
    active_processes = {}

    # 3. Start all processes
    for name, target_func in processes_to_run.items():
        process = multiprocessing.Process(target=target_func, name=name)
        process.start()
        active_processes[name] = process
    
    print("--- Multi-Source Aggregator is now RUNNING ---")

    # --- NEW: HEARTBEAT STATUS LOGIC ---
    STATUS_INTERVAL = 30  # seconds
    last_status_time = time.time()

    try:
        while True:
            # Check for and restart any failed processes
            for name, p in list(active_processes.items()):
                if not p.is_alive():
                    print(f"!!! WARNING: Process {name} has died. Restarting... !!!")
                    new_p = multiprocessing.Process(target=processes_to_run[name], name=name)
                    new_p.start()
                    active_processes[name] = new_p

            # Print the heartbeat status message
            if time.time() - last_status_time >= STATUS_INTERVAL:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                running_names = [name for name, p in active_processes.items() if p.is_alive()]
                print(f"[{timestamp}] STATUS: System healthy. Active processes: {running_names}. Awaiting new events...")
                last_status_time = time.time()

            time.sleep(5) # Check process health every 5 seconds

    except KeyboardInterrupt:
        print("\n--- Shutting down all processes ---")
        for name, p in active_processes.items():
            p.terminate()
            p.join(timeout=5) # Wait for 5 seconds for clean exit
            if p.is_alive():
                print(f"Process {name} did not terminate gracefully. Forcing kill.")
                p.kill() # Force kill if terminate fails
        print("--- Shutdown complete ---")