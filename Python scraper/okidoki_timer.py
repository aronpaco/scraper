import time
import subprocess

while True:
    print("Running okidoki_scraper.py...")
    subprocess.run(["python", "okidoki_scraper.py"])
    print("Waiting for one hour before the next execution...")
    time.sleep(3600)  
