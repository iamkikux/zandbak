from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl, validator
from typing import List
import re

app = FastAPI()

SHA256_REGEX = re.compile(r"^[a-fA-F0-9]{64}$")

class Payload(BaseModel):
    location: HttpUrl
    sha_256: List[str]

    @validator('sha_256')
    def validate_sha_list(cls, value):
        if not value:
            raise ValueError("sha_256 list must not be empty.")
        for sha in value:
            if not SHA256_REGEX.match(sha):
                raise ValueError(f"Invalid SHA-256 hash: {sha}")
        return value

@app.post("/submit")
async def submit_payload(payload: Payload):
    return {
        "message": "Payload received successfully",
        "location": payload.location,
        "sha_256": payload.sha_256
    }