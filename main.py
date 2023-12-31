from flask import Flask, request, jsonify

import requests


app = Flask(__name__)




# Replace with your Telegram bot token
BOT_TOKEN = "6526048633:AAHWo8UD4h7R64LV_R7U4YcXg-fU_7WiHLY"
# pCloud info
username = "prahladkumar3741@gmail.com"
password = "Qs%eQe@/DAHZCe4"

# Define the base URL for the Telegram Bot API
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


# Function to send a message
def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=data)
    return response.json()


# Function to handle pCloud notifications
def pcloud_notification(username, password):
    print("hello bro")


@app.route('/')
def home():
    return "Welcome to the Max Maven Bot!"


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')

        if text.startswith('/'):
            handle_commands(chat_id, text)
        else:
            send_message(chat_id, text)

    return jsonify({'status': 'ok'})


# Define command handling
def handle_commands(chat_id, command):
    if command == "/start":
        send_message(chat_id, "Hi! This is Max Maven Bot. I am always alive.")
    elif command == "/help":
        send_message(chat_id, "Sure! Here's how you can use Max Maven Bot:\n\n"
                              "/start - Start the bot\n"
                              "/help - Get help and commands\n"
                              "/about - Learn more about Max Maven Bot")
    elif command == "/about":
        send_message(chat_id, "Max Maven Bot is a simple Telegram bot created for Magic Community Group."
                              " It is created by PK Mystic")
    elif command == "/pcloud":
        pcloud_notification(username, password)
        send_message(chat_id, "Here are the recent changes in Pcloud :")
    else:
        send_message(chat_id, "I'm not sure what you mean. Use /help to see available commands.")


app.run()
