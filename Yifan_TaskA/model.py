# modules/model.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class LocalLLM:
    def __init__(
        self,
        model_name: str,
        device_map="auto",
        torch_dtype="bfloat16",
        max_new_tokens=256,
        temperature=0.2,
        top_p=0.9,
        max_input_tokens=3500,
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True
        )
        dtype = torch.bfloat16 if torch_dtype == "bfloat16" else torch.float16

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map=device_map,
            torch_dtype=dtype,
            trust_remote_code=True
        )

        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.max_input_tokens = max_input_tokens

    @torch.no_grad()
    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=self.max_input_tokens,
        ).to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=self.temperature > 0,
            temperature=self.temperature,
            top_p=self.top_p,
        )

        # ---- FIX: always access sequences ----
        if hasattr(outputs, "sequences"):
            token_ids = outputs.sequences[0]
        else:
            token_ids = outputs[0]  # fallback

        text = self.tokenizer.decode(token_ids, skip_special_tokens=True)

        return text
