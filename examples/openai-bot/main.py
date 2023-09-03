from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """Hi! You are chatting with Mercor AI, your personal assistant. I'm here to assist you toady so you can ask or talk about anything you like. Feel free to start the conversation with any question or topic, and let's have a
pleasant chat!
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):
    if "What are you?" in message_history or "Who are you?" in message_history:
        # Initialize message_history with the system prompt message
        message_history.append(SYSTEM_PROMPT)
    # Generate GPT-3.5 Turbo response
    else:
        bot_response = OpenAI.generate(
            system_prompt=SYSTEM_PROMPT,
            message_history=message_history, # Assuming history is the list of user messages
            model="gpt-3.5-turbo",
        )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": "There is some technical difficulties at the moment. We will be back soon. Thankyou for understanding."
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }