from pydantic import BaseSettings


class Settings(BaseSettings):
    token_secret_key: str
    db_connection_string: str

    class Config:
        env_file = ".env"
