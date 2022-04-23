import requests,os,json,datetime
from const.dbConnection import DbConnection
from models.monitor import Monitor
from bson.objectid import ObjectId
from fastapi import HTTPException

class ExecuteHandler:
    def __init__(self):
        self.monitors_collection = DbConnection.db['Monitors']
        self.executions_collection = DbConnection.db['Executions']
        
    def execute(self, collection_url: str, monitor_id: str):
        headers = {'Content-type': 'application/json'}
        executeResponse = requests.post(os.environ.get('EXECUTOR-URL'), data=json.dumps({"collection_url": collection_url}), headers=headers)
        executeResponseObject = json.loads(executeResponse.text)
        executeRunParams = executeResponseObject['run']
        executeRunParams['monitor_id'] = ObjectId(monitor_id)
        executeRunParams['run_time'] = datetime.datetime.now()
        db_response = self.executions_collection.insert_one(executeRunParams)
        return {"acknowledged": db_response.acknowledged, "inserted_id": str(db_response.inserted_id)}
    
    def get_executions_by_monitor_id(self, monitor_id: str):
        aggregation_pipeline = [
            {
                "$match": {
                    "monitor_id": {
                        "$eq": ObjectId(monitor_id)
                    }
                }
            },
            {
                "$project": {
                    "_id": {
                        "$toString": "$_id"
                    },
                    "monitor_id": {
                        "$toString": "$_id"
                    },
                    "stats": 1,
                    "timings": 1,
                    "executions": 1,
                    "transfers": 1,
                    "failures": 1,
                    "error": 1,
                    "run_time": 1
            }}
        ]
        
        db_response = list(self.executions_collection.aggregate(aggregation_pipeline))
        if len(db_response) > 0:
            return list(db_response)
        raise HTTPException(status_code=400, detail="There is no execution with this monitor ID")

    # def create_monitor(self, monitor: Monitor):
    #     db_response = self.monitors_collection.insert_one(monitor.__dict__)
    #     return {"acknowledged": db_response.acknowledged, "inserted_id": str(db_response.inserted_id)}

    # def update_monitor(self, monitor_id: str, monitor: Monitor):
    #     db_response = self.monitors_collection.update_one({"_id": ObjectId(monitor_id)}, {"$set": monitor.__dict__})
    #     return {"acknowledged": db_response.acknowledged, "modified_count": db_response.modified_count}
    
    # def delete_monitor(self, monitor_id: str):
    #     db_response = self.monitors_collection.delete_one({"_id": ObjectId(monitor_id)})
    #     return {"acknowledged": db_response.acknowledged, "modified_count": db_response.deleted_count}