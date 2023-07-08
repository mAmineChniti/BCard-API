from pydantic import BaseModel

class Card(BaseModel):
    name: str
    phone_number: str
    location: str
    occupation: str
    other_details: str