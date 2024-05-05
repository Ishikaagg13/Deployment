from fastapi import FastAPI
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json
from pydantic import BaseModel

app = FastAPI()


class UserData(BaseModel):
    user_input: str

# Load GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Inference endpoint
@app.post("/generate-text")
async def generate_text(input: UserData):
    prompt = input.user_input
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    generated_text_json = json.dumps({"generated_text": generated_text})
    return generated_text_json