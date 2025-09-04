from pydantic_settings import BaseSettings, SettingsConfigDict

class OpenAISettings(BaseSettings):
    """Settings for OpenAI API."""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    OPENAI_API_KEY: str
    MODEL: str = "gpt-3.5-turbo"
