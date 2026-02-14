# app/services/decomposer.py

from google import genai
import os
from dotenv import load_dotenv

from app.services.pii_masker import mask_pii
from app.services.task_classifier import classify_task
from app.services.prompt_builder import build_prompt
from app.services.post_processor import process_steps
from app.services.cache import get_cached, set_cache
from app.services.profiler import get_profile

# Load API key
load_dotenv()
client = genai.Client(api_key=os.getenv("LLM_API_KEY"))


def call_llm(prompt: str) -> str:
    """
    Calls Gemini using the new google-genai SDK
    """
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print("Gemini error:", e)
        return ""


def decompose_task(user_id: str, task_text: str):
    """
    Full decomposition pipeline:
    Profile → PII mask → classify → prompt → Gemini → post-process → cache
    """

    profile = get_profile(user_id)
    if not profile:
        return ["Create your neuro profile first"]

    # Step 1: Mask PII
    masked = mask_pii(task_text)

    # Step 2: Check cache for speed
    cached = get_cached(task_text)   # use original task
    if cached:
        return cached

    # Step 3: Classify task type
    task_type = classify_task(masked)

    # Step 4: Build profile-aware prompt
    prompt = build_prompt(masked, profile, task_type)

    # Step 5: Call Gemini
    raw = call_llm(prompt)
    if not raw:
        return ["Unable to generate steps. Try again."]

    # Step 6: Convert into atomic micro-wins
    raw_steps = raw.split("\n")
    steps = process_steps(raw_steps)

    # Step 7: Cache result
    set_cache(task_text, steps)

    return steps
