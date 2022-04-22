from fastapi import APIRouter, HTTPException
from handlers.monitor import MonitorHandler
from models.monitor import Monitor

monitor_handler = MonitorHandler()

class MonitorRouter:

    router = APIRouter(
        prefix="/monitor",
        tags=["monitor"],
        responses={404: {"description": "Not found"}},
    )

    @staticmethod
    @router.get("")
    async def get_all_monitors():
        try:
            return monitor_handler.get_all_monitors()
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)
        
    @staticmethod
    @router.get("/{monitor_id}")
    async def get_monitor_by_id(monitor_id):
        try:
            return monitor_handler.get_monitor_by_id(monitor_id)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)    
        
    @staticmethod
    @router.put("")
    async def create_monitor(monitor: Monitor):
        try:
            return monitor_handler.create_monitor(monitor)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)

    @staticmethod
    @router.post("")
    async def update_monitor(monitor_id: str, monitor: Monitor):
        try:
            return monitor_handler.update_monitor(monitor_id, monitor)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)
        
    @staticmethod
    @router.delete("")
    async def delete_monitor(monitor_id: str):
        try:
            return monitor_handler.delete_monitor(monitor_id)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)

    # @router.get("/{item_id}")
    # async def read_item(item_id: str):
    #     if item_id not in fake_items_db:
    #         raise HTTPException(status_code=404, detail="Item not found")
    #     return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


    # @router.put(
    #     "/{item_id}",
    #     tags=["custom"],
    #     responses={403: {"description": "Operation forbidden"}},
    # )
    # async def update_item(item_id: str):
    #     if item_id != "plumbus":
    #         raise HTTPException(
    #             status_code=403, detail="You can only update the item: plumbus"
    #         )
    #     return {"item_id": item_id, "name": "The great Plumbus"}