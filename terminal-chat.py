#Script remembers chat history in the terminal
from openai import OpenAI
client = OpenAI()

def generate_response(user_input, chat_history):
    chat_history.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )
    
    assistant_response = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": assistant_response})
    
    return chat_history, assistant_response

def start_chat():
    chat_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    print("General chat that remembers history")
    while True:
        user_input = input("Response: ")
        chat_history, assistant_response = generate_response(user_input, chat_history)
        print("Assistant:", assistant_response)

if __name__ == "__main__":
    start_chat()