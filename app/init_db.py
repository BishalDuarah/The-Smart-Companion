# app/init_db.py
from app.db import get_conn

def init_db():
    conn = get_conn()

    conn.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS neuro_profile (
        user_id TEXT PRIMARY KEY,
        reading_difficulty BOOLEAN,
        attention_span TEXT,
        time_blindness BOOLEAN,
        prefers_extra_steps_for TEXT,
        font_preference TEXT,
        needs_voice BOOLEAN
    );

    CREATE TABLE IF NOT EXISTS tasks (
        id TEXT PRIMARY KEY,
        user_id TEXT,
        original_task TEXT,
        masked_task TEXT,
        status TEXT
    );

    CREATE TABLE IF NOT EXISTS micro_steps (
        task_id TEXT,
        step_number INTEGER,
        step_text TEXT,
        completed BOOLEAN
    );
    """)
    conn.commit()
