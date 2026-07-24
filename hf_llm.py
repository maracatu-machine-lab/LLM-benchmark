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
        messages = [{"role": "user", "content": prompt}]

        output = self.pipe(
            messages,                    # lista de mensagens, não string
            max_new_tokens=max_tokens,
            do_sample=False,
            repetition_penalty=1.15,     # ajuda a evitar loop mesmo com greedy
            return_full_text=False,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        return output[0]["generated_text"]