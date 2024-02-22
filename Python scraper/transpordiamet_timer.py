import time
import subprocess

waiting_time = int(300) 
while True:
    print("Running okidoki_scraper.py...")
    subprocess.run(["python", "transpordiamet_scraper.py"])

    print("Waiting for", waiting_time, "seconds before the next execution...")
    time.sleep(waiting_time)  
