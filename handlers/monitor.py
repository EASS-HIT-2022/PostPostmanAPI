from const.dbConnection import DbConnection
from models.monitor import Monitor

class MonitorHandler:
    def __init__(self):
        self.monitors_collection = DbConnection.db['Monitors']

    # def get_all_monitors(self):
    #     db_response = self.monitors_collection.find()
    #     return {}

    # def create_monitor(self, monitor: Monitor):
    #     db_response = self.monitors_collection.insert_one(monitor)
    #     return {}