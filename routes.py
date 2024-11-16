from fastapi import APIRouter
from models import Profile

profile_router = APIRouter()
profiles_list = []


@profile_router.post("/profile")
async def add_profile(profile: Profile) -> dict:
    profiles_list.append(profile)
    return {"message": "Profile added successfully"}


@profile_router.get("/profile")
async def retrieve_profile() -> dict:
    return {"profiles": profiles_list}
