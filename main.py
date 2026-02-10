import requests
import time
from bs4 import BeautifulSoup

# ===== CHANGE THESE =====
EVENT_URL = "https://in.bookmyshow.com/sports/super-8-match-8-icc-men-s-t20-wc-2026/ET00474264"
TELEGRAM_TOKEN = "8500443898:AAFHtmA15oDZODTcqyq_kp1UU0nRUp96AR8"
CHAT_ID = "1349239306"
CHECK_INTERVAL = 20
# =======================


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)


def check_book_now():
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(EVENT_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if "Book Now" in soup.text:
        return True
    return False


print("Bot started...")

while True:
    try:
        print("Checking page...")

        if check_book_now():
            print("BOOK NOW FOUND!")
            send_telegram_message("🎟 Tickets are LIVE! Go Book Now!")
            break
        else:
            print("Not available yet...")

    except Exception as e:
        print("Error:", e)

    print(f"Waiting {CHECK_INTERVAL} seconds...")
    time.sleep(CHECK_INTERVAL)
