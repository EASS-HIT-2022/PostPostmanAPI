from fastapi import APIRouter, HTTPException
from handlers.execute import ExecuteHandler
from handlers.monitor import MonitorHandler
from models.monitor import Monitor

execute_handler = ExecuteHandler()
monitor_handler = MonitorHandler()

class ExecuteRouter:

    router = APIRouter(
        prefix="/executor",
        tags=["executor"],
        responses={404: {"description": "Not found"}},
    )

    @staticmethod
    @router.get("/{monitor_id}")
    async def get_all_executions_by_monitor_id(monitor_id: str):
        try:
            return execute_handler.get_executions_by_monitor_id(monitor_id)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)

    @staticmethod
    @router.post("/execute/{monitor_id}")
    async def execute_monitor(monitor_id):
        try:
            monitor = monitor_handler.get_monitor_by_id(monitor_id)
            return execute_handler.execute(monitor['collection_url'], str(monitor['_id']))
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)