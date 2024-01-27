import psycopg2
from sqlalchemy import create_engine
import os
from datetime import datetime
import requests
import pandas as pd
import json

#Retrieving my database credentials from my .env file
db_username = os.getenv('db_username')
db_password = os.getenv('db_password')
db_host = os.getenv('db_host')
db_port = os.getenv('db_port')
db_database = os.getenv('db_database')

# SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}')
print('Connection Successful')

#api_key
api_key = os.getenv('api_key')
api_key = "ac398e0864eb465d890c46b844dc2aae"


# List of currencies
currencies = ['NGN', 'GBP', 'CAD']

# Joining currency codes for the API request
currency_codes = ','.join(currencies)

# Extracting required data
api_url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols={currency_codes}"
# Check if request was successful

data = response.json()

    # Printing data in a readable format
print(json.dumps(data, indent=4))

    # Extracting base currency and timestamp
base_currency = data['base']
timestamp = data['timestamp']
readable_timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

print(f"Base Currency: {base_currency}")
print(f"Timestamp: {readable_timestamp} (UTC)")

print ('completed')