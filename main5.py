from chatbot5 import ask_ai
from prompts import SYSTEM_PROMPT
from history import load_users, save_users

all_users = load_users()

print("🤖 HR Assistant")
print("Type exit to quit")

while True:

    username = input("\nUser Name: ")

    if username.lower() == "exit":
        break

    if username not in all_users:

        all_users[username] = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    all_users[username].append(
        {
            "role": "user",
            "content": user_message
        }
    )

    reply = ask_ai(all_users[username])

    print("\nAI:", reply)

    all_users[username].append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    save_users(all_users)