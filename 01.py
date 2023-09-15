from pyrogram import Client, filters
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

bot = Client(
    "My First Project",
    api_id=8862878,
    api_hash="3052ebee93b7f4a44830119d705878bf",
    bot_token="6526048633:AAHWo8UD4h7R64LV_R7U4YcXg-fU_7WiHLY"
)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


@bot.on_message(filters.command("start") & filters.private)  # Creating a command
def start(bot, message):
    bot.send_message(message.chat.id, "Hello, I am Max Maven. I know everything about Magic")  # Calling a method


@bot.on_message(filters.command("help"))
def help(bot, message):
    bot.send_message(message.chat.id, "This is the help section of this bot")


@bot.on_message(filters.command("about"))
def about(bot, message):
    bot.send_message(message.chat.id, "This is the about section of this bot. This bot is made by Max Maven")


@bot.on_message(filters.text & filters.regex(r'^hi$'))
def command1(client, message):
    message.reply_text("Hello there!")


@bot.on_message(filters.command("notify"))
def notify(bot, message):
    bot.send_message(message.chat.id, "Getting Notifications")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://e.pcloud.com/")

    # Find the username field by class and name attributes and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.WebStyles__Input-gmVoag.caiDsQ[name="email"]')))
    username_field.send_keys("prahladkumar3741@gmail.com")

    login_button = driver.find_element(By.CLASS_NAME, "butt.submitbut.SubmitButton__Button-btzder.jEnoTE")
    login_button.click()

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.WebStyles__Input-gmVoag.caiDsQ[name="password"]')))
    password_field.send_keys('Qs%eQe@/DAHZCe4')

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

    driver.close()
    bot.send_message(message.chat.id, "New Notification arrived!")

    lines = output.strip().splitlines()
    for line in lines:
        bot.send_message(message.chat.id, line)


print("Bot Started")

bot.run()
