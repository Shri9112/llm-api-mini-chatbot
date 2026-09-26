from chat import Chat


def main():
    chat = Chat()

    print("================================")
    print("      LLM Mini Chatbot")
    print("================================")
    print("Type 'exit' to quit.")
    print("Type 'clear' to clear conversation.")
    print()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input.lower() == "clear":
            chat.clear()
            print("Conversation cleared.\n")
            continue

        response = chat.send_message(user_input)

        print(f"AI: {response}\n")


if __name__ == "__main__":
    main()