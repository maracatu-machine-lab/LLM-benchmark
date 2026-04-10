from hf_llm import HuggingFaceLLM


def load_model(name: str):
    
    models = {
        "medgemma": "unsloth/medgemma-4b-it", # -> Funcionou
        "gemma-br": "CEIA-UFG/Gemma-3-Gaia-PT-BR-4b-it", # -> Funcionou
        "phi-4-mini": "microsoft/Phi-4-mini-instruct", # -> Funcionou
        "qwen-3.5": "techwithsergiu/Qwen3.5-text-4B",  # -> Funcionou
        "llama": "meta-llama/Llama-2-7b", # -> GATED
        "meta-llama": "meta-llama/Llama-3.2-1B",# -> GATED
        "t5-pt": "unicamp-dl/ptt5-base-portuguese-vocab", # -> ERRO DE LIB (TIKTOKEN / SPIECE MODEL)
        "latam-gpt": "latam-gpt/Wayra-Perplexity-Estimator-55M", # -> NÃO RECONHECEU A ARQUITETURA
        "clinical": "pucpr-br/Clinical-BR-LlaMA-2-7B", # -> TIMEOUT
        "medgemma-pt": "pucpr-br/medgemma-pt-finetuned-multiclinsum", # -> NÃO TEM A PROPRIEDADE MODEL_TYPE CONFIGURADA
        "gemma": "google/gemma-4-31B-it" #-> Mais de 65GB e não executou
    }

    if name not in models:
        raise ValueError(f"Modelo '{name}' não suportado")

    hf_token = 'INSIRA-SEU-TOKEN-DO-HUGGING-FACE'

    return HuggingFaceLLM(models[name], hf_token)

#Llama-3.2   Gemma-3