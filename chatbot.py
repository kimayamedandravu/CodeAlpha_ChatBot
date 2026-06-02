print("🤖 Kimaya's ChatBot")
print("Type 'bye' to end the chat.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello there! 😊")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: I'm Kimaya's ChatBot.")

    elif user == "good morning":
        print("Bot: Good morning! Have a productive day.")

    elif user ==  "thank you": 
        print("Bot: You're welcome!")

    elif user == "what can you do":
        print("Bot: I can chat with you, answer simple questions, and keep you company!")
        
    elif user == "bye":
        print("Bot: Goodbye! Take care. 👋")
        break

    else:
        print("Bot: Hmm... I don't know how to respond to that yet.")
