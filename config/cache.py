from os import environ
from dotenv import load_dotenv
from redis import Redis
from pathlib import Path

dotenv_path = Path('/etc/secrets/.env')
load_dotenv(dotenv_path=dotenv_path)

reduser = environ.get('REDUSER')
redpassword = environ.get('REDPASSWORD')
redhostname = environ.get('REDHOSTNAME')
redport = environ.get('REDPORT')
# Create a Redis client
redis_client = Redis(host=f"rediss://{reduser}:{redpassword}@{redhostname}", port=redport, decode_responses=True)
