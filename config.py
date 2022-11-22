from pydantic import BaseSettings


class Settings(BaseSettings):
    token_secret_key: str

    class Config:
        env_file = ".env"
