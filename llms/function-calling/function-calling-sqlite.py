import json
import ollama
import asyncio
import sqlite3

def get_antonyms(word: str) -> str:
    "Get the antonyms of the any given word"

    words = {
        "hot": "cold",
        "small": "big",
        "weak": "strong",
        "light": "dark",
        "lighten": "darken",
        "dark": "bright",
    }

    return json.dumps(words.get(word, "Not available in database"))


# In a real application, this would fetch data from a live database or API
def get_flight_times(departure: str, arrival: str) -> str:
    try:
        # Tạo và kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('flights.db')
        cursor = conn.cursor()

        route = f"{departure.upper()}-{arrival.upper()}"
        cursor.execute('SELECT * FROM flights WHERE route = ?', (route,))
        flight = cursor.fetchone()
        if flight:
            return {
                "route": flight[1],
                "departure": flight[2],
                "arrival": flight[3],
                "duration": flight[4]
            }
        else:
            return {"error": "Flight not found"}

    except():
        print('error')
    finally:
        # Đóng kết nối với cơ sở dữ liệu
        conn.close()

    key = f"{departure}-{arrival}".upper()
    return json.dumps(flight.get(key, {"error": "Flight not found"}))


async def run(model: str, user_input: str):
    client = ollama.AsyncClient()
    # Initialize conversation with a user query
    messages = [
        {
            "role": "user",
            "content": user_input,
            # "content": "What is the capital of India?",
        }
    ]

    # First API call: Send the query and function description to the model
    response = await client.chat(
        model=model,
        messages=messages,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_flight_times",
                    "description": "Get the flight times between two cities",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "departure": {
                                "type": "string",
                                "description": "The departure city (airport code)",
                            },
                            "arrival": {
                                "type": "string",
                                "description": "The arrival city (airport code)",
                            },
                        },
                        "required": ["departure", "arrival"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_antonyms",
                    "description": "Get the antonyms of any given words",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "word": {
                                "type": "string",
                                "description": "The word for which the opposite is required.",
                            },
                        },
                        "required": ["word"],
                    },
                },
            },
        ],
    )

    print(f"AI Response: {response}\n")

    # Add the model's response to the conversation history
    messages.append(response["message"])

    print(f"Conversation history:\n{messages}")

    # Check if the model decided to use the provided function
    if not response["message"].get("tool_calls"):
        print("\nThe model didn't use the function. Its response was:")
        print(response["message"]["content"])
        return

    if response["message"].get("tool_calls"):
        # print(f"\nThe model used some tools")
        available_functions = {
            "get_flight_times": get_flight_times,
            "get_antonyms": get_antonyms,
        }
        # print(f"\navailable_function: {available_functions}")
        for tool in response["message"]["tool_calls"]:
            # print(f"available tools: {tool}")
            # tool: {'function': {'name': 'get_flight_times', 'arguments': {'arrival': 'LAX', 'departure': 'NYC'}}}
            function_to_call = available_functions[tool["function"]["name"]]
            print(f"function to call: {function_to_call}")

            if function_to_call == get_flight_times:
                function_response = function_to_call(
                    tool["function"]["arguments"]["departure"],
                    tool["function"]["arguments"]["arrival"],
                )
                print(f"function response: {function_response}")

            elif function_to_call == get_antonyms:
                function_response = function_to_call(
                    tool["function"]["arguments"]["word"],
                )
                print(f"function response: {function_response}")

            messages.append(
                {
                    "role": "tool",
                    "content": function_response,
                }
            )


while True:
    user_input = input("\n Please ask=> ")
    if not user_input:
        user_input = "What is the flight time from NYC to LAX?"
    if user_input.lower() == "exit":
        break

    asyncio.run(run("llama3.1", user_input))