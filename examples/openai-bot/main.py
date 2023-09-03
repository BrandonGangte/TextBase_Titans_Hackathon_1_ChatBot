from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = ""

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """Hi!\U0001F920 You are chatting with Mercor AI, your personal assistant. I'm here to assist you today, so you can ask or talk about anything you like. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!"""

def calculate_order_total():
    # Define the list of orders inside the function
    orders = [
        {"item": "Toothpaste", "price": 2.99},
        {"item": "Shampoo", "price": 5.95},
        {"item": "Bread", "price": 2.49},
        {"item": "Milk", "price": 3.99},
        {"item": "Eggs", "price": 1.99},
        {"item": "Soap", "price": 1.49},
        {"item": "Toilet Paper", "price": 6.29},
        {"item": "Laundry Detergent", "price": 8.99},
        {"item": "Paper Towels", "price": 4.79},
        {"item": "Deodorant", "price": 3.49},
        {"item": "Orange Juice", "price": 3.29},
        {"item": "Cereal", "price": 4.59},
        {"item": "Apples", "price": 0.99},
        {"item": "Bananas", "price": 0.69},
        {"item": "Potatoes", "price": 1.29},
    ]


    total_price = 0.0  # Initialize the total price to zero

    # Initialize an empty string to capture the output
    output_str = ""
    selected_orders = orders[-5:]
    # Iterate through the list of orders
    for order in selected_orders:
        item_name = order["item"]
        item_price = order["price"]

        # Add the item and its price to the output string
        output_str += f"{item_name}: ${item_price:.2f}\n\n"

        # Add the item price to the total
        total_price += item_price

    # Add the total price to the output string
    output_str += f"Total: ${total_price:.2f}"

    # Return the output string as the result
    return output_str


def get_weather_condition(day,text):
    # Split the text by "Today:"
    parts = text.split(day)
   # print(parts)

    if len(parts) > 1:
        # Extract the weather condition after "Today:"
        weather_condition = parts[1].strip()
        print("Check this " + weather_condition)
        return weather_condition

    return None


def get_weather_icon_url(weather_condition):
    # Define a dictionary to map weather conditions to image URLs
    weather_icons = {
        "Mostly sunny": "G:\TitansHackathon\TextBase_Titans_Hackathon_1_ChatBot\docs\src\image\sun.png",  # Replace with actual URLs
        "Partly cloudy": "G:\TitansHackathon\TextBase_Titans_Hackathon_1_ChatBot\docs\src\image\cloud.png",
        "Rainy": "G:\TitansHackathon\TextBase_Titans_Hackathon_1_ChatBot\docs\src\image\rainy.png",
        "Snowy": "G:\TitansHackathon\TextBase_Titans_Hackathon_1_ChatBot\docs\src\image\snowy.png",
    }
    # Return the URL based on the weather condition
    return weather_icons.get(weather_condition, "G:\TitansHackathon\TextBase_Titans_Hackathon_1_ChatBot\docs\src\image\sun.png")  # Default for unknown conditions


@bot()
def on_message(message_history: List[Message], state: dict = None):
    user_message = message_history[-1]["content"][0]["value"]

    if "track my order" in user_message:
        # Extract the order number from the user's message
        # Example function call with no arguments
        total = calculate_order_total()
        response = f"Certainly!\U0001F60A  Here are the list of products you purchased:\n\n"
        response += total
    elif "What are you?" in user_message or "Who are you?" in user_message:
            # Initialize message_history with the system prompt message
            response = SYSTEM_PROMPT
        # Generate GPT-3.5 Turbo response
    else:
        bot_response = OpenAI.generate(
            system_prompt=SYSTEM_PROMPT,
            message_history=message_history, # Assuming history is the list of user messages
            model="gpt-3.5-turbo",
         )
        response = bot_response

    if "--" in user_message:
        weather_condition1 = get_weather_condition("Today:",bot_response)
        weather_condition2 = get_weather_condition("Tomorrow:",bot_response)
        weather_condition3 = get_weather_condition("Day after tomorrow:",bot_response)
        return {
            "status_code": 200,
            "response": {
                "data": {
                    "messages": [
                        {
                            "data_type": "STRING",
                            "value": "Weather forecast for the next three days:",
                        },
                        {
                            "data_type": "STRING",
                            "value": "Today: "+ weather_condition1,
                        },
                        {
                            "data_type": "IMAGE",
                            "value": "<img src='G:\TitansHackathon\TextBase_Titans_Hackathon_1_ChatBot\docs\src\image\sun.png' alt='Sun Icon' width='32' height='32'>",
                        },
                        {
                            "data_type": "STRING",
                            "value": "Tomorrow: "+ weather_condition2,
                        },
                        {
                            "data_type": "IMAGE",
                            "value": get_weather_icon_url(weather_condition2),
                        },
                        {
                            "data_type": "STRING",
                            "value": "Day after tomorrow: "+weather_condition3,
                        },
                        {
                            "data_type": "IMAGE",
                            "value": get_weather_icon_url(weather_condition3),
                        }
                    ],
                    "state": state
                },
                "errors": [
                    {
                        "message": "There are some technical difficulties at the moment. We will be back soon. Thank you for understanding."
                    }
                ]
            }
        }
    else:
        return {
            "status_code": 200,
            "response": {
                "data": {
                    "messages": [
                        {
                            "data_type": "STRING",
                            "value": response
                        }
                    ],
                    "state": state
                },
                "errors": [
                    {
                        "message": "There are some technical difficulties at the moment. We will be back soon. Thank you for understanding."
                    }
                ]
            }
        }

