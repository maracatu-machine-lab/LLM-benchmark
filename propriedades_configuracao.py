from pydantic_settings import BaseSettings
from pydantic import field_validator
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    hf_token: str 

    @field_validator("hf_token")
    def validar_token(cls, v):
        if "SEU-TOKEN-AQUI" in v:
            raise ValueError("Você precisa configurar seu HF_TOKEN no .env")
        return v

    timeout_in_seconds: int = 900 # 5 minutos
    numero_iteracoes: int = 1

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()