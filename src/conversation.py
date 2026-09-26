class Conversation:
        def __init__(self):
            self.history = []

        def add_user_message(self, message):
            self.history.append({
                "role": "user",
                "text": message
            })

        def add_assistant_message(self, message):
            self.history.append({
                "role": "assistant",
                "text": message
            })

        def get_history(self):
            return self.history

        def build_prompt(self):
            conversation = ""

            for message in self.history:
                conversation += f'{message["role"]}: {message["text"]}\n'

            return conversation
        
        def clear(self):
            self.history = []


# if __name__ == "__main__":
#     conversation = Conversation()

#     conversation.add_user_message("My name is Shri.")
#     conversation.add_assistant_message("Nice to meet you, Shri.")
#     conversation.add_user_message("I am learning AI engineering.")

#     print(conversation.get_history())

#     print("\n--- BUILT PROMPT ---")
#     print(conversation.build_prompt())

#     conversation.clear()

#     print("\n--- AFTER CLEAR ---")
#     print(conversation.get_history())
