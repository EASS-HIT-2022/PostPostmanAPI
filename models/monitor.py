from pydantic import BaseModel
from typing import Optional

class Monitor(BaseModel):
    name: str
    description: Optional[str] = None
    collection_data: dict