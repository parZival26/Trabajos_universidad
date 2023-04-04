import openai
openai.api_key = "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"

def chat_gpt(prompt):
    try:
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        return completion.choices[0].message.content
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        pregunta = input("Ingresa tu pregunta: \n")
        if pregunta == "exit": break
        else: print(f"\n {chat_gpt(pregunta)} \n")
