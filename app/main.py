from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.init_db import init_db
from app.api.profile import router as profile_router
from app.api.task import router as task_router

app = FastAPI()

# ✅ CORS MUST be added immediately after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(profile_router)
app.include_router(task_router)
app.mount("/ui", StaticFiles(directory="frontend/smart-ui/dist", html=True), name="static")



@app.get("/")
def root():
    return {"message": "Smart Companion API running"}
