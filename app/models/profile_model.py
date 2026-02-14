from pydantic import BaseModel
from typing import List

class ProfileModel(BaseModel):
    reading_difficulty: bool
    attention_span: str
    time_blindness: bool
    prefers_extra_steps_for: List[str]
    font_preference: str
    needs_voice: bool
