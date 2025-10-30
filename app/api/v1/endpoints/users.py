from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def read_users():
    return [{"id": 1, "name": "示例用户1"}, {"id": 2, "name": "示例用户2"}]

@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"id": user_id, "name": f"示例用户{user_id}"}