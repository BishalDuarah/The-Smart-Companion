import uuid
from app.db import get_conn
from app.crypto import encrypt, decrypt


def create_task(user_id: str, original_task: str, masked_task: str, steps: list):
    conn = get_conn()
    task_id = str(uuid.uuid4())

    conn.execute("""
        INSERT INTO tasks (id, user_id, original_task, masked_task, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        task_id,
        user_id,
        encrypt(original_task),
        encrypt(masked_task),
        "in_progress"
    ))

    for i, step in enumerate(steps):
        conn.execute("""
            INSERT INTO micro_steps (task_id, step_number, step_text, completed)
            VALUES (?, ?, ?, ?)
        """, (
            task_id,
            i,
            encrypt(step),
            False
        ))

    conn.commit()
    return task_id


def get_steps(task_id: str):
    conn = get_conn()
    rows = conn.execute("""
        SELECT step_number, step_text, completed
        FROM micro_steps
        WHERE task_id=?
        ORDER BY step_number
    """, (task_id,)).fetchall()

    steps = []
    for r in rows:
        steps.append({
            "step_number": r[0],
            "step_text": decrypt(r[1]),
            "completed": bool(r[2])
        })

    return steps


def complete_step(task_id: str, step_number: int):
    conn = get_conn()
    conn.execute("""
        UPDATE micro_steps
        SET completed=1
        WHERE task_id=? AND step_number=?
    """, (task_id, step_number))
    conn.commit()
