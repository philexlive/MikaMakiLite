import os
import dotenv
import yaml
import re
from typing import Optional, Self

dotenv.load_dotenv()


class TgConfig:
    api_id: str = os.getenv("TG_API_ID")
    api_hash: str = os.getenv("TG_API_HASH")
    session: str = os.getenv("TG_SESSION")
    chat_id: tuple[int, int]

    def __init__(self, chat_id: str | None = None):
        if not chat_id is None: 
            self.set_chat(chat_id)

    def set_chat(self, chat_id: str) -> Self:
        new_id = re.split(r"_", chat_id)
        self.chat_id = tuple(int(i) for i in new_id)
        return self


class CharacterConfig:
    class AIInfo:
        api_key: str = os.getenv("HF_API_KEY")
        
        def __init__(self, model, provider, who):
            self.model: str = model
            self.provider: str = provider
            self.who: str = who
        
    def __init__(self):
        self.ai: CharacterConfig.AIInfo = None
        self.watermark: str = None
        try:
            with open("src/config/character.yaml") as stream:
                data = yaml.safe_load(stream)
                
                ai_conf = data["ai"]
                self.ai = CharacterConfig.AIInfo(
                    model=ai_conf["model"],
                    provider = ai_conf["provider"],
                    who = ai_conf["who"]
                )

                self.watermark = data["watermark"]
        except yaml.YAMLError as e:
            print(e)


character_config = CharacterConfig()
tg_config = TgConfig(
    chat_id=os.getenv("DEFAULT_CHAT_ID")
)

dotenv.load_dotenv()