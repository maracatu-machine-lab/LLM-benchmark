from transformers import pipeline, AutoConfig, AutoModelForSeq2SeqLM, AutoModelForCausalLM, AutoTokenizer, GenerationConfig
import torch
from interface_base import BaseLLM


class HuggingFaceLLM(BaseLLM):
    def __init__(self, model_name: str, hf_token: str = None):
        self.model_name = model_name

        config = AutoConfig.from_pretrained(model_name, token=hf_token)
        # Detecta tipo do modelo automaticamente e usa do cache ou baixa os pesos
        if config.is_encoder_decoder:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name, token=hf_token)
            task = "text2text-generation"
        else:
            # Pode acessar localmente como "./models/medgemma"
            self.model = AutoModelForCausalLM.from_pretrained(model_name, token=hf_token)
            task = "text-generation"


        self.tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)

        self.device = 0 if torch.cuda.is_available() else -1
        self.pipe = pipeline(
            task,
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )
        
        self.pipe = pipeline(
            task,
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )

    def generate(self, prompt: str, max_tokens: int = 100) -> str:
        output = self.pipe(
            prompt,
            max_new_tokens=max_tokens,
            do_sample=False,
            return_full_text=False
        )
        return output[0]["generated_text"]