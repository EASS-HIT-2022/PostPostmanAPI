#PostPostman API
The API can give you the information about the system's monitor.

The API is working with MongoDB with 2 collections:
Monitors - saves administrative data of monitors objects.
Ececutions - save data of monitor executions by monitor id.

Routes:
**/monitors:**
create, read (also read all), update and delete operations for monitor object
**/executor:**
/{monitor_id} - get all the executions of the given monitor
/execute/{monitor_id} - run the given monitor (run data will be saved to DB)