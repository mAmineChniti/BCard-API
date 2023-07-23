import redis
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from micro.services import process_card
from config.database import collection_name
from schemas.cardschema import cards_serialize
from os import environ
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/etc/secrets/.env')
load_dotenv(dotenv_path=dotenv_path)
redhost = environ.get('REDHOST')

BCardrouter = APIRouter()

# Create a Redis client
redis_client = redis.Redis(host=redhost, port=6379, decode_responses=True)

# Redirection to documentation page
@BCardrouter.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')

# API Status check
@BCardrouter.get("/status", include_in_schema=False)
async def status():
    return {"status": "ok"}

# Save text from front in a MongoDB database
@BCardrouter.post('/save_card')
def save_card(user_id: str, text: str):
    try:
        result = process_card(text)

        # Add user_id to the result dictionary
        result["_id"] = user_id

        # Store the entire result dictionary in MongoDB
        collection_name.insert_one(result)

        # Invalidate the cache for the user_id, as the data has changed
        redis_client.delete(user_id)

        return {"message": "Card saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route to get all cards of a user with Redis caching
@BCardrouter.get('/cards')
def user_cards(user_id: str):
    try:
        # Check if the data is already cached in Redis
        cached_data = redis_client.get(user_id)
        if cached_data:
            return JSONResponse(content=cached_data)

        # Query MongoDB collection for cards of the specified user_id
        cards = collection_name.find({"_id": user_id})

        # Serialize the cards
        serialized_cards = cards_serialize(cards)
        
        # Cache the data in Redis for future requests
        redis_client.set(user_id, serialized_cards)

        return JSONResponse(content=serialized_cards)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
