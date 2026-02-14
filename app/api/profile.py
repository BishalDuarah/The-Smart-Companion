from fastapi import APIRouter, Request
from app.services.profiler import create_profile, get_profile

router = APIRouter()

@router.post("/profile/{user_id}")
async def create(user_id: str, request: Request):
    data = await request.json()
    print("Incoming profile data:", data)  # 👈 will show in terminal

    create_profile(user_id, data)
    return {"message": "Profile created"}

@router.get("/profile/{user_id}")
def fetch(user_id: str):
    profile = get_profile(user_id)
    return profile
