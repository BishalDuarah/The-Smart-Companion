# app/services/task_classifier.py
def classify_task(text: str) -> str:
    text = text.lower()
    if "kitchen" in text or "cook" in text:
        return "kitchen"
    if "study" in text or "exam" in text:
        return "study"
    if "email" in text or "office" in text:
        return "work"
    return "general"
