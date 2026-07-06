from hf_llm import HuggingFaceLLM
from propriedades_configuracao import settings

MODELOS_DISPONIVEIS = {
    "medgemma": "unsloth/medgemma-4b-it",
    "gemma-br": "CEIA-UFG/Gemma-3-Gaia-PT-BR-4b-it",
    "phi-4-mini": "microsoft/Phi-4-mini-instruct",
    "qwen-3.5": "techwithsergiu/Qwen3.5-text-4B",
}

def carregar_modelo(nome: str):
    if nome not in MODELOS_DISPONIVEIS:
        raise ValueError(f"Modelo '{nome}' não suportado")

    hf_token = settings.hf_token

    return HuggingFaceLLM(MODELOS_DISPONIVEIS[nome], hf_token)