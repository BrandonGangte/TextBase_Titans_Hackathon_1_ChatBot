from pydantic import BaseModel
from typing import List, Dict
import random

class Content(BaseModel):
    data_type: str
    value: str

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: List[Content]

