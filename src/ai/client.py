from src.config import character_config
from huggingface_hub import InferenceClient


inference = InferenceClient(
    model=character_config.ai.model, 
    provider=character_config.ai.provider
)