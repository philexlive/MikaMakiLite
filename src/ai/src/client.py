import os

from pydantic import BaseModel, Field
from pydantic_ai import Agent

import src.sources.huggingface_source
import src.sources.mistral_source

from .config.persona import persona


# Text response of model
class ClientResponse(BaseModel):
    text: str = Field(description="Client responded.")


# Setup an Agent
ai_client = Agent(
    model,
    output_type=ClientResponse,
    instructions=(
        'Your identity.'
        'Name: {name}'
        'Bio:'
        '{bio}'
    ).format(
        name=persona.name,
        bio=persona.bio
    ),
    end_strategy='exhaustive'
)


@ai_client.tool_plain
def write_code(filename: str, code: str):
    """Writes the script to the file.
    
    Keyword arguments:
    filename: str -- a name of the file code will be written to.
    code: str -- entire code will be written to a file.
    """

    if not os.path.isdir("response"):
        os.mkdir("response")
    
    with open(f"response/{filename}", 'w') as f:
        f.write(code)