import re
import json

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)    # remove urls
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_items(items):
    for item in items:
        combined = f"{item['title']} - {item['description']}"
        item["clean_text"] = clean_text(combined)
    return items
