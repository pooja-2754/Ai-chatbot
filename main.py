from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

conversation = []


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=conversation
    )

    answer = response.choices[0].message.content

    print("AI:", answer)

    conversation.append({
        "role": "assistant",
        "content": answer
    })

    # response = client.chat.completions.create(
    #     model="openai/gpt-oss-120b",
    #     messages=[
    #         {"role": "user", "content": user_input}
    #     ]
    # )

    # print("Bot:", response.choices[0].message.content)