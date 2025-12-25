from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic_ai.models import Model


class AISource(BaseModel):
    model_name: str
    api_key: Optional[str]

    model_config = ConfigDict(extra='ignore')

    def build(self) -> Model:
        raise NotImplementedError

