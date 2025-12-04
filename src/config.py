import os
import dotenv

dotenv.load_dotenv()

CHAT=int(os.getenv("CHAT_ID"))
TOPIC=int(os.getenv("TOPIC_ID"))