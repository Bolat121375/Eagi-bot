from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from handlers import register_handlers
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == '__main__':
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
