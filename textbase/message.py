from pydantic import BaseModel
from typing import List
import random

class Content(BaseModel):
    data_type: str
    value: str

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: List[Content]

# Define possible greetings
greetings = ["Hello!", "Hi there!", "Welcome!", "Greetings!", "Good day!"]

# Define possible questions to engage the user
questions = [
    "How can I assist you today?",
    "Is there anything specific you'd like to know?",
    "What brings you here?",
    "Do you have any questions or concerns?",
]

# Define supportive responses
support_responses = [
    "I'm here to help!",
    "Feel free to ask anything; I'm at your service.",
    "Don't hesitate to reach out if you need assistance.",
    "You're in good hands! How can I assist you?",
]

def generate_welcome_message():
    return random.choice(greetings)

def generate_question():
    return random.choice(questions)

def generate_supportive_response():
    return random.choice(support_responses)

# Simulate a conversation
conversation = []

# Initial welcome message
conversation.append(Message(role="assistant", content=[Content(data_type="STRING", value=generate_welcome_message())]))

# User responds
#conversation.append(Message(role="user", content=[Content(data_type="STRING", value="Hi!")]))

# Assistant generates a question
conversation.append(Message(role="assistant", content=[Content(data_type="STRING", value=generate_question())]))

# User responds
conversation.append(Message(role="user", content=[Content(data_type="STRING", value="I have a question about your products.")]))

# Assistant provides a supportive response
conversation.append(Message(role="assistant", content=[Content(data_type="STRING", value=generate_supportive_response())]))

# Continue the conversation as needed...

# Print the conversation
for message in conversation:
    print(f"{message.role.capitalize()}: {message.content[0].value}")
