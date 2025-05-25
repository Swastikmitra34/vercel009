from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load student marks from JSON file once
with open("q-vercel-python.json") as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = []):
    marks = [student_marks.get(n, 0) for n in name]
    return {"marks": marks}

