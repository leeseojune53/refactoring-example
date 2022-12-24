from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name):
    return {"message": f"Hello {name}"}


@router.post("/user",
             tags=["user"],
             responses={201: {"description": "created"}})
async def create_user(user_id: str, user_name: str):
    return {"user_id": user_id, "user_name": user_name}