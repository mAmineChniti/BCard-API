import spacy

nlp = spacy.load("en_core_web_md")

def process_card(text):
    doc = nlp(text)
    
    result = {}
    
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
            result["other_details"] = entity.text
    
    return result
