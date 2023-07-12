def card_serialize(Card) -> dict:
    return {
        "user_id": Card.get("user_id"),
        "name": Card.get("name"),
        "phone_number": Card.get("phone_number"),
        "location": Card.get("location"),
        "occupation": Card.get("occupation"),
        "email": Card.get("email"),
        "other_details": Card.get("other_details")
    }

def cards_serialize(Cards) -> list:
    return [card_serialize(Card) for Card in Cards if Card is not None]