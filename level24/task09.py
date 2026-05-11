import openai

def get_openai_response(api_key, prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

api_key = input("Digite sua chave de API da OpenAI: ")
prompt = input("Digite sua consulta para o modelo ChatGPT: ")
response = get_openai_response(api_key, prompt)
print("Resposta do modelo ChatGPT:")
print(response)