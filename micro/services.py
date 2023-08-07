from spacy import load
from os import path

model_directory = path.join(path.dirname(__file__), 'BCard_Model_1.1')

# Load the custom model
nlp = load(model_directory)

def process_card(text):
    doc = nlp(text)
    
    result = {
        "name": None,
        "phone_number": None,
        "location": None,
        "occupation": None,
        "email": None,
        "company": None,
        "other_details": []
    }
    
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            result["name"] = entity.text
        elif entity.label_ == "PHONE_NUMBER":
            result["phone_number"] = entity.text
        elif entity.label_ == "GPE":
            result["location"] = entity.text
        elif entity.label_ == "OCCUPATION":
            result["occupation"] = entity.text
        elif entity.label_ == "EMAIL":
            result["email"] = entity.text
        elif entity.label_ == "COMPANY":
            result["company"] = entity.text
        else:
            result["other_details"].append(entity.text)
    
    result["other_details"] = ' '.join(result["other_details"])
    
    return result