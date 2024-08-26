from pydantic_settings import BaseSettings


class Secrets(BaseSettings):
    TOKEN: str
    SUPABASE_URL: str
    SUPABASE_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


secrets = Secrets()
