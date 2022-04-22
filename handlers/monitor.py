from const.dbConnection import DbConnection
from models.monitor import Monitor
from bson.objectid import ObjectId
from fastapi import HTTPException

class MonitorHandler:
    def __init__(self):
        self.monitors_collection = DbConnection.db['Monitors']

    def get_all_monitors(self):
        aggregation_pipeline = [
            {
                "$project": {
                    "_id": {
                        "$toString": "$_id"
                    },
                    "name": 1,
                    "description": 1,
                    "collection_data": 1
            }}
        ]
        
        db_response = self.monitors_collection.aggregate(aggregation_pipeline)
        return list(db_response)
    
    def get_monitor_by_id(self, monitor_id: str):
        aggregation_pipeline = [
            {
                "$match": {
                    "_id": {
                        "$eq": ObjectId(monitor_id)
                    }
                }
            },
            {
                "$project": {
                    "_id": {
                        "$toString": "$_id"
                    },
                    "name": 1,
                    "description": 1,
                    "collection_data": 1
            }}
        ]
        
        db_response = self.monitors_collection.aggregate(aggregation_pipeline)
        if len(list(db_response)) > 0:
            return list(db_response)[0]
        raise HTTPException(status_code=400, detail="There is no monitor with this ID")

    def create_monitor(self, monitor: Monitor):
        db_response = self.monitors_collection.insert_one(monitor.__dict__)
        return {"acknowledged": db_response.acknowledged, "inserted_id": str(db_response.inserted_id)}

    def update_monitor(self, monitor_id: str, monitor: Monitor):
        db_response = self.monitors_collection.update_one({"_id": ObjectId(monitor_id)}, {"$set": monitor.__dict__})
        return {"acknowledged": db_response.acknowledged, "modified_count": db_response.modified_count}
    
    def delete_monitor(self, monitor_id: str):
        db_response = self.monitors_collection.delete_one({"_id": ObjectId(monitor_id)})
        return {"acknowledged": db_response.acknowledged, "modified_count": db_response.deleted_count}