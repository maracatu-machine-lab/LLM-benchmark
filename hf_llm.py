from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, GenerationConfig
import torch
from interface_base import BaseLLM


class HuggingFaceLLM(BaseLLM):
    def __init__(self, model_name: str, hf_token: str = None):
        self.model_name = model_name

        self.device = 0 if torch.cuda.is_available() else -1

        # Detecta tipo do modelo automaticamente e usa do cache ou baixa os pesos
        if "t5" in model_name.lower():
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name, local_files_only=True)
        else:
            # Pode acessar localmente como "./models/medgemma"
            self.model = AutoModelForCausalLM.from_pretrained(model_name)

        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token)

        self.pipe = pipeline(
            "text-generation" if not "t5" in model_name.lower() else "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )

    def generate(self, prompt: str, max_tokens: int = 200) -> str:
        config = GenerationConfig(
            max_new_tokens=max_tokens,
            temperature=0.7,
            do_sample=True
        )

        output = self.pipe(prompt, generation_config=config)

        return output[0]["generated_text"]