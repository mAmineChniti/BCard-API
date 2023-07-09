import spacy

def process_card(input_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    
    result = {
        "name": None,
        "phone_number": None,
        "location": None,
        "occupation": None,
        "other_details": None
    }
    
    entities = [ent.text for ent in doc.ents]
    for entity in entities:
        if result["name"] is None and entity.istitle():
            result["name"] = entity
        elif result["phone_number"] is None and entity.startswith(("(", "+")):
            result["phone_number"] = entity
        elif result["location"] is None and entity.endswith(("Street", "Avenue")):
            result["location"] = entity
        elif result["occupation"] is None and "Manager" in entity:
            result["occupation"] = entity
    
    details = []
    for token in doc:
        if token.pos_ == "NUM":
            details.append(token.text)
        elif token.pos_ == "PROPN":
            details.append(token.text)
        elif token.like_email:
            details.append(token.text)
        elif token.like_url:
            details.append(token.text)
    
    if details:
        result["other_details"] = "\n".join(details)
    
    return result
