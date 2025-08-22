from pydantic import BaseModel

from app.src.shared.settings import settings


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    exp: int = settings.access_token_expire_minutes * 60
