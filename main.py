import requests
import json

# Replace with your Telegram bot token
BOT_TOKEN = "6526048633:AAHWo8UD4h7R64LV_R7U4YcXg-fU_7WiHLY"

# Define the base URL for the Telegram Bot API
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"offset": offset, "timeout": 60}
    response = requests.get(url, params=params)
    return response.json()


def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=data)
    return response.json()


def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates.get("result", []):
            message = update.get("message")
            chat_id = message.get("chat").get("id")
            text = message.get("text")

            if text:
                send_message(chat_id, text)

            # Set the new offset to avoid processing the same update again
            offset = update.get("update_id") + 1



main()
