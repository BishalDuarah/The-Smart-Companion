from fastapi import APIRouter
from app.services.decomposer import decompose_task
from app.services.pii_masker import mask_pii
from app.services.task_manager import create_task, get_steps, complete_step

router = APIRouter()

@router.post("/task/{user_id}")
def create(user_id: str, data: dict):
    task_text = data["task"]

    # Generate micro steps
    steps = decompose_task(user_id, task_text)

    # Mask PII for storage
    masked = mask_pii(task_text)

    # Store in DB
    task_id = create_task(user_id, task_text, masked, steps)

    return {"task_id": task_id}


@router.get("/steps/{task_id}")
def fetch(task_id: str):
    return {"steps": get_steps(task_id)}


@router.post("/step/complete")
def mark_done(data: dict):
    complete_step(data["task_id"], data["step_number"])
    return {"message": "Step marked complete"}

