from llm_client import generate_response
from conversation import Conversation

class Chat:

    def __init__(self):
        self.conversation = Conversation()

    def send_message(self, user_message):
        self.conversation.add_user_message(user_message)

        prompt = self.conversation.build_prompt()

        response = generate_response(prompt)

        self.conversation.add_assistant_message(response)

        return response
    
    def clear(self):
        self.conversation.clear()

# if __name__ == "__main__":
#     chat = Chat()

#     response = chat.send_message("My name is Shri.")
#     print("AI:", response)

#     response = chat.send_message("What is my name?")
#     print("AI:", response)