from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from services.weather_api import get_weather

def register_handlers(dp: Dispatcher):

    @dp.message_handler(Command("start"))
    async def start_command(message: types.Message):
        await message.reply("Привет! Напиши название города, и я пришлю сводку погоды.")

    @dp.message_handler()
    async def weather_request(message: types.Message):
        weather_info = get_weather(message.text)
        await message.reply(weather_info)