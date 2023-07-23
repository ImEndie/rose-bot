from telebot import TeleBot
import os
from dotenv import load_dotenv

load_dotenv()

bot=TeleBot(token=os.getenv("BOT_TOKEN"),parse_mode="MARKDOWN")
