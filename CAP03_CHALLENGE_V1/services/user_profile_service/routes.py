from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
user_profiles = {}
next_id = 1

class UserProfileIn(BaseModel):
    name: str
    email: str

class UserProfileOut(UserProfileIn):
    id: int

@router.post("/user_profiles/", status_code=201, response_model=UserProfileOut)
def create_user_profile(profile: UserProfileIn):
    global next_id
    profile_data = profile.model_dump()
    profile_data["id"] = next_id
    user_profiles[next_id] = profile_data
    next_id += 1
    return profile_data

@router.get("/user_profiles/{profile_id}", response_model=UserProfileOut)
def get_user_profile(profile_id: int):
    if profile_id not in user_profiles:
        raise HTTPException(status_code=404, detail="Profile not found")
    return user_profiles[profile_id]

@router.put("/user_profiles/{profile_id}", response_model=UserProfileOut)
def update_user_profile(profile_id: int, profile: UserProfileIn):
    if profile_id not in user_profiles:
        raise HTTPException(status_code=404, detail="Profile not found")
    profile_data = profile.model_dump()
    profile_data["id"] = profile_id
    user_profiles[profile_id] = profile_data
    return profile_data

@router.delete("/user_profiles/{profile_id}", status_code=204)
def delete_user_profile(profile_id: int):
    if profile_id not in user_profiles:
        raise HTTPException(status_code=404, detail="Profile not found")
    del user_profiles[profile_id]
    return