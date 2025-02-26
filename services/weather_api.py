import requests
import datetime
import math
import logging
from config import WEATHER_API_URL, WEATHER_API_KEY, DEFAULT_LANGUAGE, DEFAULT_UNITS
from helpers.weather_icons import weather_icons
from helpers.logger import get_logger

logger = get_logger(__name__)

def get_weather(city: str):
    if not city.strip():
        return "Ошибка! Название города не может быть пустым."

    params = {
        "q": city,
        "lang": DEFAULT_LANGUAGE,
        "appid": WEATHER_API_KEY,
        "units": DEFAULT_UNITS,
    }
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            return "Ошибка! Город не найден."
        return format_weather_data(data)
    except requests.RequestException as e:
        logging.error(f"Ошибка запроса: {e}")
        return "Ошибка! Не удалось получить данные о погоде."


def format_weather_data(data: dict):
    city = data.get("name")
    if not city:
        return "Ошибка! Город не найден."

    weather_info = [
        f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Погода в городе: {city}"
    ]

    temp = data["main"].get("temp")
    if temp is not None:
        weather_desc = data["weather"][0].get("main", "")
        weather_icon = weather_icons.get(weather_desc, "")
        weather_info.append(f"Температура: {round(temp, 1)}°C {weather_icon}")

    humidity = data["main"].get("humidity")
    if humidity is not None:
        weather_info.append(f"Влажность: {humidity}%")

    pressure = data["main"].get("pressure")
    if pressure is not None:
        weather_info.append(f"Давление: {math.ceil(pressure / 1.333)} мм.рт.ст")

    wind = data["wind"].get("speed")
    if wind is not None:
        weather_info.append(f"Ветер: {wind} м/с")

    sunrise = data["sys"].get("sunrise")
    if sunrise:
        weather_info.append(f"Восход солнца: {datetime.datetime.fromtimestamp(sunrise).strftime('%H:%M')}")

    sunset = data["sys"].get("sunset")
    if sunset:
        weather_info.append(f"Закат солнца: {datetime.datetime.fromtimestamp(sunset).strftime('%H:%M')}")

    weather_info.append("Хорошего дня!")

    return "\n".join(weather_info)