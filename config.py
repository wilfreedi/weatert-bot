from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
DEFAULT_LANGUAGE = 'ru'
DEFAULT_UNITS = "metric"
