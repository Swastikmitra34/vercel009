from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data (assuming you have this file in root or /api)
with open("api/q-vercel-python.json") as f:
    student_marks = json.load(f)

@app.get("/")
async def get_marks(name: list[str] = []):
    marks = [student_marks.get(n, 0) for n in name]
    return {"marks": marks}
