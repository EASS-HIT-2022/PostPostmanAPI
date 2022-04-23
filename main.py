from fastapi import FastAPI
from routers import monitor, execute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(monitor.MonitorRouter.router)
app.include_router(execute.ExecuteRouter.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)