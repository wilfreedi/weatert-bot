from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import TELEGRAM_API_TOKEN
from handlers import register_handlers
from helpers.logger import get_logger

logger = get_logger(__name__)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp)