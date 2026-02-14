# app/services/profiler.py
import json
from app.db import get_conn
from app.crypto import encrypt, decrypt

def create_profile(user_id: str, data: dict):
    conn = get_conn()

    encrypted_profile = encrypt(json.dumps(data))

    conn.execute("""
        INSERT OR REPLACE INTO neuro_profile (user_id, reading_difficulty, attention_span,
        time_blindness, prefers_extra_steps_for, font_preference, needs_voice)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        data["reading_difficulty"],
        data["attention_span"],
        data["time_blindness"],
        encrypt(json.dumps(data["prefers_extra_steps_for"])),
        data["font_preference"],
        data["needs_voice"]
    ))

    conn.commit()


def get_profile(user_id: str):
    conn = get_conn()
    row = conn.execute("""
        SELECT * FROM neuro_profile WHERE user_id=?
    """, (user_id,)).fetchone()

    if not row:
        return None

    return {
        "reading_difficulty": row[1],
        "attention_span": row[2],
        "time_blindness": row[3],
        "prefers_extra_steps_for": json.loads(decrypt(row[4])),
        "font_preference": row[5],
        "needs_voice": row[6]
    }
