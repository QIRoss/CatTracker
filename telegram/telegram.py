import telebot
import os
from choose_picture import choose_picture

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6646406153:AAF6YOTeoqBKuBP--6vszBwr5GXSrPnx7ss'

# Initialize the Telegram bot
bot = telebot.TeleBot(TOKEN)

# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello! I am your picture bot. Send /sendpic to get a picture.')

@bot.message_handler(commands=['sendpic'])
def send_picture(message):
    # Check if the picture file exists
    picture_path = choose_picture()
    if os.path.exists(picture_path):
        # Send the picture
        with open(picture_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Picture not found.')

@bot.message_handler(commands=['sendgif'])
def send_gif(message):
    # Replace 'path_to_gif.gif' with the actual path to your GIF file
    gif_path = 'cat.gif'
    # Check if the GIF file exists
    if os.path.exists(gif_path):
        # Send the GIF
        with open(gif_path, 'rb') as gif:
            bot.send_animation(message.chat.id, gif)
    else:
        bot.send_message(message.chat.id, 'GIF not found.')

# Start the bot
bot.polling()
