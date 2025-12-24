import asyncio

from src.services.ai_service import AIService

async def main():
    service = AIService()
    await service.run()
 
if __name__ == "__main__":
    asyncio.run(main())