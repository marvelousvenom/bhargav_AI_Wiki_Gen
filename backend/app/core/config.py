from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Wiki Quiz Generator"

    DATABASE_URL: str

   
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
