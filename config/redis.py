from os import environ
from dotenv import load_dotenv
from pathlib import Path
import redis

dotenv_path = Path('/etc/secrets/.env')
load_dotenv(dotenv_path=dotenv_path)
redhost = environ.get('REDHOST')
redport = environ.get('REDPORT')

# Create a Redis client
redis_client = redis.Redis(host=redhost, port=redport, decode_responses=True)
