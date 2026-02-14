# app/services/pii_masker.py
import re

def mask_pii(text: str) -> str:
    text = re.sub(r'\b[A-Z][a-z]+\b', '[NAME]', text)
    text = re.sub(r'\b\d{10}\b', '[PHONE]', text)
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    text = re.sub(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', '[DATE]', text)
    return text
