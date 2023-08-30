import random
import time

# Predefined responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how_are_you": ["I'm doing well, thanks!", "I'm good. How about you?", "I'm great!"],
    "name": ["You can call me Robo Chatbot.", "I'm Robo Chatbot.", "I don't have a name, but you can call me Robo Chatbot."],
    "weather": ["I'm just a text-based chatbot and don't have access to real-time data. You can check a weather website for that!"],
    "health": ["I'm not a doctor, but maintaining a healthy lifestyle through proper diet and exercise is important.",
               "Remember to stay hydrated and get enough sleep for overall well-being.",
               "If you have specific health concerns, it's best to consult a medical professional."],
    "time": ["The current time is " + time.strftime("%H:%M") + ".", "It's currently " + time.strftime("%I:%M %p") + "."],
    "current_date": ["Today's date is " + time.strftime("%Y-%m-%d") + ".", "It's " + time.strftime("%A, %B %d, %Y") + "."],
    "chatbot_specs": ["I'm a rule-based chatbot programmed in Python.",
                      "I can answer questions about weather, health, time, and more.",
                      "I'm designed to provide predefined responses based on user input."],
    "who_are_you": ["I'm Robo Chatbot, a friendly AI designed to assist and chat with you.",
                    "I'm your virtual assistant, here to engage in conversations and answer your questions.",
                    "I'm an AI language model developed by OpenAI, ready to assist you."],
    "goodbye": ["Goodbye!", "Have a great day!", "Take care!"],
    "movie_suggestions": ["I recommend checking out movies like Inception, The Shawshank Redemption, or Avengers: Endgame.",
                          "If you're into comedy, try watching The Grand Budapest Hotel or Deadpool.",
                          "For a thrilling experience, consider watching The Dark Knight or Mad Max: Fury Road."],
    "book_suggestions": ["You might enjoy reading books like 1984 by George Orwell, To Kill a Mockingbird by Harper Lee, or The Great Gatsby by F. Scott Fitzgerald.",
                         "If you're into fantasy, give the Harry Potter series by J.K. Rowling or The Lord of the Rings by J.R.R. Tolkien a try.",
                         "For non-fiction, consider reading Sapiens by Yuval Noah Harari or Educated by Tara Westover."],
    "learning_website_suggestions": ["For online learning, you can explore platforms like Coursera, Udemy, and Khan Academy.",
                                     "If you're interested in programming, Codecademy and freeCodeCamp offer coding tutorials.",
                                     "For language learning, Duolingo and Babbel are popular choices."],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "Interesting. Tell me more."]
}

conversation_history = []

# Function to generate chatbot responses based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return random.choice(responses["hello"])
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    elif "who are you" in user_input:
        return random.choice(responses["who_are_you"])
    elif "your name" in user_input:
        return random.choice(responses["name"])
    elif "weather" in user_input:
        return random.choice(responses["weather"])
    elif "health" in user_input:
        return random.choice(responses["health"])
    elif "time" in user_input and "date" in user_input:
        return random.choice(responses["time"]) + " " + random.choice(responses["current_date"])
    elif "chatbot" in user_input and ("what can you do" in user_input or "tell me about yourself" in user_input):
        return random.choice(responses["chatbot_specs"])
    elif "movie" in user_input and "suggest" in user_input:
        return random.choice(responses["movie_suggestions"])
    elif "book" in user_input and "suggest" in user_input:
        return random.choice(responses["book_suggestions"])
    elif "learning website" in user_input and ("suggest" in user_input or "recommend" in user_input):
        return random.choice(responses["learning_website_suggestions"])
    elif any(goodbye_word in user_input for goodbye_word in ["bye", "goodbye", "see you"]):
        return random.choice(responses["goodbye"])
    else:
        return random.choice(responses["default"])

# Chat loop
print("Robo Chatbot: Hi I'm a Robo Chatbot! How can I help you today? (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    conversation_history.append("You: " + user_input)
    
    if user_input.lower() == "exit":
        print("Robo Chatbot:", random.choice(responses["goodbye"]))
        break
    
    response = chatbot_response(user_input)
    conversation_history.append("Robo Chatbot: " + response)
    print("Robo Chatbot:", response)