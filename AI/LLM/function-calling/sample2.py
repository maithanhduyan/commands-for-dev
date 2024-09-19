import ollama

# Dữ liệu chuyến bay
flights = {
    "NYC-LAX": {
        "departure": "08:00 AM",
        "arrival": "11:30 AM",
        "duration": "5h 30m",
    },
    "LAX-NYC": {
        "departure": "02:00 PM",
        "arrival": "10:30 PM",
        "duration": "5h 30m",
    },
    "LHR-JFK": {
        "departure": "10:00 AM",
        "arrival": "01:00 PM",
        "duration": "8h 00m",
    },
    "JFK-LHR": {
        "departure": "09:00 PM",
        "arrival": "09:00 AM",
        "duration": "7h 00m",
    },
    "CDG-DXB": {
        "departure": "11:00 AM",
        "arrival": "08:00 PM",
        "duration": "6h 00m",
    },
    "DXB-CDG": {
        "departure": "03:00 AM",
        "arrival": "07:30 AM",
        "duration": "7h 30m",
    },
}

# Hàm tìm chuyến bay dựa trên mã chuyến bay
def find_flight(flight_code):
    if flight_code in flights:
        flight = flights[flight_code]
        return f"Flight {flight_code}: Departure at {flight['departure']}, Arrival at {flight['arrival']}, Duration {flight['duration']}"
    else:
        return f"Flight {flight_code} not found."

# Hàm gọi LLaMA qua ollama để tìm chuyến bay
def search_flight_with_llama(flight_code):
    query = f"Find details for the flight {flight_code}."
    
    # Gọi mô hình LLaMA 3.1 với ollama
    response = ollama.chat(model="llama3.1", tools=[
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
        }
    ])
    
    # Hiển thị kết quả
    flight_info = find_flight(flight_code)
    return flight_info

# Chạy thử nghiệm với một chuyến bay
flight_code = "NYC-LAX"
flight_details = search_flight_with_llama(flight_code)
print(flight_details)
