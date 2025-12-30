from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "hackathon-secret"
ALGORITHM = "HS256"

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=6)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
