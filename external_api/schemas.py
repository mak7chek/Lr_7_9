from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from .config import settings as cfg
#  Модель для Жарту
class JokeModel(BaseModel):
    joke: str = Field(
        ...,
        description="Text of the random joke",
        min_length=cfg.min_joke_length,
        max_length=cfg.max_joke_length,
    )
    id: int = Field(..., description="ID of the joke")

    model_config: ConfigDict = ConfigDict(from_attributes=True)


# Модель для Мему
class MemeModel(BaseModel):
    url: HttpUrl = Field(
        ...,
        description="URL of the random meme image",
        min_length=cfg.min_url_length,
        max_length=cfg.max_url_length,
    )
    id: int = Field(..., description="ID of the meme")

    model_config: ConfigDict = ConfigDict(from_attributes=True)


class HumorCombinedModel(BaseModel):
    joke_text: str = Field(
        ...,
        description="Text of the joke",
        min_length=cfg.min_joke_length,
        max_length=cfg.max_joke_length,
    )
    meme_url: HttpUrl = Field(
        ...,
        description="URL of the meme image",
        min_length=cfg.min_url_length,
        max_length=cfg.max_url_length,
    )

    source: str = Field("HumorAPI", description="Data provider")

    model_config: ConfigDict = ConfigDict(from_attributes=True)