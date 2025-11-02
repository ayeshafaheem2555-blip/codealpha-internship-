print("🤖 ChatBot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("🤖 ChatBot: Goodbye! Have a great day! 👋")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("🤖 ChatBot: Hi there! How can I help you today?")
    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm just a program, but I'm doing great! 😄 How about you?")
    elif "your name" in user_input:
        print("🤖 ChatBot: I'm ChatGPT Jr., your Python-made bot!")
    elif "python" in user_input:
        print("🤖 ChatBot: Python is an awesome language — easy and powerful! 🐍")
    elif "time" in user_input:
        from datetime import datetime
        print("🤖 ChatBot: Current time is", datetime.now().strftime("%H:%M:%S"))
    elif "internship" in user_input:
        print("🤖 ChatBot: Internships are a great way to learn real-world skills! Are you doing one with CodeAlpha?")
    elif "codealpha" in user_input:
        print("🤖 ChatBot: That’s awesome! CodeAlpha offers great learning opportunities 🚀 Keep growing!")
    elif "certificate" in user_input:
        print("🤖 ChatBot: Congratulations on earning your certificate! 🎓 Every milestone counts!")
    elif "thank" in user_input:
        print("🤖 ChatBot: You're most welcome! 😊 Always here to help.")
    else:
        print("🤖 ChatBot: Sorry, I don’t understand that. Can you rephrase?")
