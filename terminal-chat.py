from openai import OpenAI

client = OpenAI()

def chat_with_gpt(prompt, engine="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                        {"role": "system", "content": "You are a cybersecurity assistant"},
                        {"role": "user", "content": prompt}
                    ],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def start_chat():
    print("Welcome to ChatGPT Chat! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting chat. Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")

if __name__ == "__main__":
    start_chat()