from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def read_items():
    return [{"id": 1, "name": "示例项目1"}, {"id": 2, "name": "示例项目2"}]

@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"id": item_id, "name": f"示例项目{item_id}"}