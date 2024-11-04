from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
CLOUD_PASSWORD = os.getenv('CLOUD_PASSWORD')

if not all((API_ID, API_HASH, PHONE_NUMBER, CLOUD_PASSWORD)):
    raise ValueError("Something went wrong with .env file")
