from aiogram import Router, types
from aiogram.filters import Command
from services.weather_api import get_weather

router = Router()

def register_handlers(dp):
    dp.include_router(router)

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши название города, и я пришлю сводку погоды.")

@router.message()
async def weather_request(message: types.Message):
    weather_info = get_weather(message.text)
    await message.reply(weather_info)
