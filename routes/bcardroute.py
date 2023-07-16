from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from micro.services import process_card
from config.database import collection_name
from schemas.cardschema import cards_serialize

BCardrouter = APIRouter()

# Redirection to documentation page
@BCardrouter.get("/",include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')

# API Status check
@BCardrouter.get("/status",include_in_schema=False)
async def status():
    return {"status":"ok"}

# Save text from front in a mongodb database
@BCardrouter.post('/save_card')
def save_card(user_id: str, text: str):
    try:
        result = process_card(text)

        # Add user_id to the result dictionary
        result["_id"] = user_id

        # Store the entire result dictionary in MongoDB
        collection_name.insert_one(result)

        return {"message": "Card saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route to get all cards of a user
@BCardrouter.get('/cards')
def user_cards(user_id: str):
    try:
        # Query MongoDB collection for cards of the specified user_id
        cards = collection_name.find({"_id": user_id})
        
        # Serialize the cards
        serialized_cards = cards_serialize(cards)
        
        return JSONResponse(content=serialized_cards)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))