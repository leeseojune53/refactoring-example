from fastapi import FastAPI
from app.router import user

app = FastAPI()

app.include_router(user.router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
