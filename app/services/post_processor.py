import re

def clean_text(step: str) -> str:
    # Remove numbering
    step = re.sub(r'^\d+\.\s*', '', step)

    # Remove brackets content
    step = re.sub(r'\(.*?\)', '', step)

    # Remove trailing punctuation
    step = step.strip().rstrip('.').strip()

    return step


def split_into_atomic(step: str):
    # Split by commas, and, then
    parts = re.split(r',|\band\b|\bthen\b', step)

    final_parts = []
    for p in parts:
        p = p.strip()
        if len(p.split()) >= 2:
            final_parts.append(p)

    return final_parts


def clean_step(step: str):
    step = clean_text(step)

    words = step.split()
    if len(words) > 14:
        step = " ".join(words[:14])

    step = step.capitalize()
    return step


def process_steps(raw_steps):
    final_steps = []

    for step in raw_steps:
        atomic_parts = split_into_atomic(step)

        for part in atomic_parts:
            cleaned = clean_step(part)
            final_steps.append(cleaned)

    return final_steps
