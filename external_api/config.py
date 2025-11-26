from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    humor_api_key: str

    min_joke_length: int = 5
    max_joke_length: int = 3000
    min_url_length: int = 10
    max_url_length: int = 2048

    class Config:
        env_file = ".env"


settings = Settings()