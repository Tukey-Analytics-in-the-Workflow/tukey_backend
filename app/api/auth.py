from fastapi import APIRouter, Depends, HTTPException
from app.security.jwt import create_token

router = APIRouter()

@router.post("/login")
def login(email: str, password: str):
    # MVP: hardcoded user
    if email != "admin@tukey.ai":
        raise HTTPException(401)

    token = create_token({"sub": email, "role": "admin"})
    return {"access_token": token}
