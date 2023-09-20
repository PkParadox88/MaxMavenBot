from flask import Flask, request, jsonify

import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)


# Configure Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://e.pcloud.com/")

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
    # Find the username field by class and name attributes and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.WebStyles__Input-gmVoag.caiDsQ[name="email"]')))
    username_field.send_keys(username)

    login_button = driver.find_element(By.CLASS_NAME, "butt.submitbut.SubmitButton__Button-btzder.jEnoTE")
    login_button.click()

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.WebStyles__Input-gmVoag.caiDsQ[name="password"]')))
    password_field.send_keys(password)

    submit_button = driver.find_element(By.CLASS_NAME, 'SubmitButton__Button-btzder.jEnoTE')
    submit_button.click()

    print('Login Successfully !!')
    time.sleep(5)

    # wait for the bell icon to be clickable and click it
    bell_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.NotificationsBell__NotificationsBellLight-fpUEGl.gRBuVI')))
    bell_icon.click()

    notifications = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.NotificationsPopoverWrap__NotificationsInner-ciUPXa.QyHmz')))
    output = str(notifications.text)
    print(output)


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
