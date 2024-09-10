import sqlite3

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

# Tạo và kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('flights.db')
cursor = conn.cursor()

# Tạo bảng flights
cursor.execute('''
CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route TEXT NOT NULL,
    departure TEXT NOT NULL,
    arrival TEXT NOT NULL,
    duration TEXT NOT NULL
)
''')

# Insert dữ liệu từ flights vào bảng
for route, data in flights.items():
    cursor.execute('''
    INSERT INTO flights (route, departure, arrival, duration)
    VALUES (?, ?, ?, ?)
    ''', (route, data['departure'], data['arrival'], data['duration']))

# Lưu thay đổi vào cơ sở dữ liệu
conn.commit()

# Hàm tìm chuyến bay từ cơ sở dữ liệu
def find_flight(departure: str, arrival: str):
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

# Ví dụ sử dụng hàm find_flight
flight_info = find_flight("NYC", "LAX")
print(flight_info)

# Đóng kết nối với cơ sở dữ liệu
conn.close()
