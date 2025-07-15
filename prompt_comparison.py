import openai


openai.api_key = "Your_Api_Key"


prompt = input("Enter your prompt: ")


response_35 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\n🔷 GPT-3.5 Response:\n")
print(response_35['choices'][0]['message']['content'])




with open("prompt_results.txt", "a", encoding="utf-8") as file:
    file.write(f"\nPrompt: {prompt}\n")
    file.write("GPT-3.5:\n" + response_35['choices'][0]['message']['content'] + "\n")
    file.write("="*60 + "\n")
