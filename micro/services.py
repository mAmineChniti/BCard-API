import re

def extract_name(text):
    lines = text.split("\n")
    return lines[0]

def extract_phone_number(text):
    phone_regex = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    matches = re.findall(phone_regex, text)
    if matches:
        return matches[0]
    return None

def extract_location(text):
    lines = text.split("\n")
    location_line = [line for line in lines if re.search(r'\b\d{5}\b', line)]
    if location_line:
        return location_line[0]
    return None

def extract_occupation(text):
    lines = text.split("\n")
    occupation_line = [line for line in lines if re.search(r'\b[A-Za-z]+\b\s+Manager', line)]
    if occupation_line:
        return occupation_line[0]
    return None

def extract_other_details(text):
    lines = text.split("\n")
    details = lines[1:-1]
    if details:
        return "\n".join(details)
    return None

def process_card(input_text):
    result = {
        "name": None,
        "phone_number": None,
        "location": None,
        "occupation": None,
        "other_details": None
    }
    
    result["name"] = extract_name(input_text)
    result["phone_number"] = extract_phone_number(input_text)
    result["location"] = extract_location(input_text)
    result["occupation"] = extract_occupation(input_text)
    result["other_details"] = extract_other_details(input_text)
    
    return result