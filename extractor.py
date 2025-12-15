
import re

SUSPICIOUS_WORDS = [
    "urgent", "verify", "password", "click", "account",
    "confirm", "bank", "login", "update"
]

def extract_features(text):
    features = {}
    features["num_links"] = len(re.findall(r"http[s]?://", text))
    features["contains_suspicious_words"] = any(word in text.lower() for word in SUSPICIOUS_WORDS)
    features["num_digits"] = sum(char.isdigit() for char in text)
    return features