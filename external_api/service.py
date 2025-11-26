import httpx
from .schemas import JokeModel, MemeModel, HumorCombinedModel
from .config import settings

class HumorService:
    def __init__(self):
        self.api_key = settings.humor_api_key
        self.base_url = "https://api.humorapi.com"

    async def get_joke(self) -> JokeModel:
        url = f"{self.base_url}/jokes/random"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params={"api-key": self.api_key})
            response.raise_for_status()
            data = response.json()

            return JokeModel(**data)

    async def get_meme(self) -> MemeModel:
        url = f"{self.base_url}/memes/random"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params={"api-key": self.api_key})
            response.raise_for_status()
            data = response.json()

            return MemeModel(**data)

    async def get_combined_humor(self) -> HumorCombinedModel:
        joke = await self.get_joke()
        meme = await self.get_meme()
        return HumorCombinedModel(
            joke_text=joke.joke,
            meme_url=meme.url,
            source="HumorAPI via Service Layer"
        )


humor_service = HumorService()