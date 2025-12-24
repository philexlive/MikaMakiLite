from typing import Optional

from pydantic import BaseModel
from pydantic_ai.models import Model


class AISource(BaseModel):
    model_name: str

    provider_name: Optional[str]
    base_url: Optional[str]
    
    api_key: str

    def build(self) -> Model:
        raise NotImplementedError

