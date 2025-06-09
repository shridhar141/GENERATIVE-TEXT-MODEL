from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

print("Enter your prompt (type 'exit' to quit):")

while True:
    prompt = input(">> ").strip()
    if prompt.lower() == "exit":
        break
    if not prompt:
        print("Please enter some text.")
        continue

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_length=100,
        do_sample=True,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nGenerated Text:\n" + "-"*50)
    print(generated_text)
    print("-" * 50)
