from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    hf_token: str

    @field_validator("hf_token")
    def validar_token(cls, v):
        if "coloque_seu_token" in v:
            raise ValueError("Você precisa configurar seu HF_TOKEN no .env")
        return v

    timeout_in_seconds: int = 300 # 5 minutos
    numero_iteracoes: int = 10

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()