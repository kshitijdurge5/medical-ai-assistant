import os
from dotenv import load_dotenv
from openai import OpenAI


print("[1/6] Loading environment variables...")

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()

if api_key == "":
    raise SystemExit(
        "DEEPSEEK_API_KEY was not found. "
        "Please add it to your .env file."
    )


print("[2/6] Creating DeepSeek client...")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


print("[3/6] Getting your question...")

user_question = input(
    "What medical topic would you like to learn about? "
)


messages = [
    {
        "role": "system",
        "content": (
            "You are an AI medical education assistant. "
            "You explain medical topics in simple language. "
            "Help beginners understand medicine and surgery. "
            "Explain difficult concepts step by step. "
            "Give examples when useful. "
            "Do not pretend to replace a real doctor."
        ),
    },
    {
        "role": "user",
        "content": user_question
    }
]


print("\n[4/6] Messages being sent to DeepSeek:")
print(messages)


print("\n[5/6] Sending request to DeepSeek...")


try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=0.3,
        max_tokens=700
    )

except Exception as error:
    print("[ERROR] The API call failed.")
    print("Reason:", error)
    raise


answer = response.choices[0].message.content


print("\n[6/6] AI Medical Assistant:")
print("--------------------------------")
print(answer)
print("--------------------------------")