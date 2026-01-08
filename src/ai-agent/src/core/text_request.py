from typing import Optional

from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    behaviour: str = Field(description='Specific behaviour setting')
    sender_initials: str = Field(description='Sender\'s initials of the name')
    text: str = Field(description='The message of the sender')