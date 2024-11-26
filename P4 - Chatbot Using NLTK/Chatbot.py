import nltk
from nltk.chat.util import Chat, reflections
from tkinter import Tk, Label, Button, Text, Scrollbar, Entry

# Download necessary NLTK packages
nltk.download('punkt')

# Define some basic patterns for the chatbot
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I assist you?"]),
    (r"how are you?", ["I'm doing great, thank you for asking!", "I'm good, how are you?"]),
    (r"what is your name?", ["I am your friendly chatbot!", "I don't have a name, but I can chat with you!"]),
    (r"(.*) (your|my) name?", ["My name is Chatbot!", "I am Chatbot, what's your name?"]),
    (r"(.*) (help|assist)(.*)", ["Sure! How can I assist you today?", "I am here to help you. What do you need?"]),
    (r"quit", ["Goodbye!", "See you later!", "Take care!"]),
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Define function to process user input and generate response
def get_response():
    user_input = user_entry.get()
    if user_input.lower() == "quit":
        chat_box.insert("end", "You: " + user_input + "\n")
        chat_box.insert("end", "Chatbot: Goodbye! Take care.\n")
        window.quit()
    else:
        response = chatbot.respond(user_input)
        chat_box.insert("end", "You: " + user_input + "\n")
        chat_box.insert("end", "Chatbot: " + response + "\n")
        user_entry.delete(0, "end")
        chat_box.yview(END)

# Create the GUI using Tkinter
window = Tk()
window.title("Chatbot")

# Set up the chat window layout
chat_box = Text(window, height=20, width=50, wrap="word")
scrollbar = Scrollbar(window, command=chat_box.yview)
chat_box.config(yscrollcommand=scrollbar.set)
chat_box.grid(row=0, column=0, padx=10, pady=10)
scrollbar.grid(row=0, column=1, sticky="ns")

user_entry = Entry(window, width=40, font=("Arial", 14))
user_entry.grid(row=1, column=0, padx=10, pady=10)

send_button = Button(window, text="Send", command=get_response, width=10, bg="#4CAF50", fg="white")
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter main loop
window.mainloop()
