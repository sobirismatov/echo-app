from flask import Flask, request, jsonify
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os

# flask app
app = Flask(__name__)

# telegram bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)

@app.route('/')
def index():
    return 'ok'

@app.route('/api', methods=['POST'])
def api():
    update = Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat_id
    text = update.message.text

    bot.send_message(chat_id=update.message.chat_id, text=text)

    return jsonify({'ok': True})
