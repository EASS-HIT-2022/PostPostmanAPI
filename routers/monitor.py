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