from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel

router = APIRouter()

fake_users_db = {}

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register", status_code=201)
def register(user: UserRegister):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.username] = {"username": user.username, "password": user.password}
    return {"message": "User created successfully"} 

@router.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)
    if not db_user or db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": f"fake-jwt-token-for-{user.username}"}

@router.get("/users/me")
def get_current_user(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ")[1]
    # Simulación: extrae el username del token
    if token.startswith("fake-jwt-token-for-"):
        username = token.replace("fake-jwt-token-for-", "")
        if username in fake_users_db:
            return {"username": username}
    raise HTTPException(status_code=401, detail="Invalid token")