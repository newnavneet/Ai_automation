# This is a mock/demo version that does NOT call OpenAI API (no internet or API key needed)

def fake_gpt_response(prompt, model_name):
    if "java" in prompt.lower():
        return f"{model_name} says: Java is a high-level, class-based, object-oriented programming language used for building applications."
    else:
        return f"{model_name} says: Sorry, I'm just a mock model. I can't answer this fully!"

prompt = input("Enter your prompt: ")

response_35 = fake_gpt_response(prompt, "GPT-3.5")
response_4 = fake_gpt_response(prompt, "GPT-4")


print("\n🔷 GPT-3.5 Response:\n")
print(response_35)

print("\n🟣 GPT-4 Response:\n")
print(response_4)


with open("prompt_results.txt", "a", encoding="utf-8") as file:
    file.write(f"\nPrompt: {prompt}\n")
    file.write("GPT-3.5:\n" + response_35 + "\n")
    file.write("GPT-4:\n" + response_4 + "\n")
    file.write("="*60 + "\n")
