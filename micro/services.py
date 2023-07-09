import spacy
nlp = spacy.load("en_core_web_sm")

def process_card(text):
    doc = nlp(text)
    
    result = {
        "name": None,
        "phone_number": None,
        "location": None,
        "occupation": None,
        "other_details": None
    }
    
    for entity in doc.ents:
        if entity.label_ == "PERSON" and not result["name"]:
            result["name"] = entity.text
        elif entity.label_ == "PHONE_NUMBER" and not result["phone_number"]:
            result["phone_number"] = entity.text
        elif entity.label_ == "GPE" and not result["location"]:
            result["location"] = entity.text
        elif entity.label_ == "OCCUPATION" and not result["occupation"]:
            result["occupation"] = entity.text
        elif not result["other_details"]:
            result["other_details"] = entity.text
    
    return result