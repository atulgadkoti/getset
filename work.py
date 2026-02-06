import requests
import schedule
import time
from config import API_URL

def make_request():
    """Make a GET request to the URL"""
    try:
        response = requests.get(API_URL)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}")  # Print first 200 chars
    except Exception as e:
        print(f"Error: {e}")

# Schedule the request to run every 10 minutes
schedule.every(10).minutes.do(make_request)

print("Scheduler started. Making requests every 10 minutes...")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)
