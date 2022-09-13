from datetime import datetime
import string
from pydantic import BaseModel


class TodoRequest(BaseModel):
    title: str
    description: str
