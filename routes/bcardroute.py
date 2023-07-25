from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from micro.services import process_card
from config.database import bcards_collection
from config.cache import redis_client
from schemas.cardschema import cards_serialize
import asyncio

BCardrouter = APIRouter()

# Redirection to documentation page
@BCardrouter.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url='/docs')

# API Status check
@BCardrouter.get("/status", include_in_schema=False)
async def status():
    try:
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Save text from front in a MongoDB database
@BCardrouter.post('/save_card')
async def save_card(user_id: str, text: str):
    try:
        result = await process_card(text)

        # Add user_id to the result dictionary
        result["_id"] = user_id

        # Store the entire result dictionary in MongoDB
        await bcards_collection.insert_one(result)

        # Invalidate the cache for the user_id, as the data has changed
        await redis_client.delete(user_id)

        return {"message": "Card saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route to get all cards of a user with Redis caching
@BCardrouter.get('/cards')
async def user_cards(user_id: str):
    try:
        # Check if the data is already cached in Redis
        cached_data = await redis_client.get(user_id)
        if cached_data:
            return JSONResponse(content=cached_data)

        # Query MongoDB collection for cards of the specified user_id
        cards = await bcards_collection.find({"_id": user_id})

        # Serialize the cards
        serialized_cards = cards_serialize(cards)

        # Cache the data in Redis for future requests
        await redis_client.set(user_id, serialized_cards)

        return JSONResponse(content=serialized_cards)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
