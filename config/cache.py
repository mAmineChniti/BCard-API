from os import environ
from dotenv import load_dotenv
import redis

load_dotenv('/etc/secrets/.env')
redhost = environ.get('REDHOST')
redport = environ.get('REDPORT')

# Create a Redis client
redis_client = redis.Redis(host=redhost, port=redport, decode_responses=True)
