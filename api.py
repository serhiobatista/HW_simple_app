from fastapi import FastAPI
from routes import profile_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}
app.include_router(profile_router)
