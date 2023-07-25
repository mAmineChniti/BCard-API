from os import environ
from dotenv import load_dotenv
import redis

load_dotenv('/etc/secrets/.env')
reduser = environ.get('REDUSER')
redpassword = environ.get('REDPASSWORD')
redhostname = environ.get('REDHOSTNAME')
redport = environ.get('REDPORT')
# Create a Redis client
redis_client = redis.Redis(host=f"rediss://{reduser}:{redpassword}@{redhostname}", port=redport, decode_responses=True)
