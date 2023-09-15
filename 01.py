from pyrogram import Client, filters

bot = Client(
    "My First Project",
    api_id=8862878,
    api_hash="3052ebee93b7f4a44830119d705878bf",
    bot_token="6526048633:AAHWo8UD4h7R64LV_R7U4YcXg-fU_7WiHLY"
)


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


print("Bot Started")

bot.run()
