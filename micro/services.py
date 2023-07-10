import spacy
import os

model_directory = os.path.join(os.path.dirname(__file__), 'custom_model')

# Load the custom model
nlp = spacy.load(model_directory)

def process_card(text):
    doc = nlp(text)
    
    result = {
        "name": None,
        "phone_number": None,
        "location": None,
        "occupation": None,
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
        else:
            result["other_details"].append(entity.text)
    
    result["other_details"] = ' '.join(result["other_details"])
    
    return result