from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

class TextMessage(BaseModel):
    recipient_id: str
    message_text: str


class PhotoMessage(BaseModel):
    recipient_id: str
    image_url: str
    is_reusable: bool


class SuccessMessage(BaseModel):
    recipient_id: str
    message_id: str