import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import TELEGRAM_API_TOKEN
from handlers import register_handlers
from helpers.logger import get_logger

logger = get_logger(__name__)

# Создаем бота с новыми настройками
bot = Bot(token=TELEGRAM_API_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# Регистрируем хендлеры
register_handlers(dp)

async def main():
    logger.info("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
