from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    PROJECT_NAME: str = "AI Wiki Quiz Generator"

    # Database
    DATABASE_URL: str

    # API Keys
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
