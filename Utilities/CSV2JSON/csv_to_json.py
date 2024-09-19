import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Đọc dữ liệu từ file CSV
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []
        for row in csv_reader:
            data.append(row)

    # Ghi dữ liệu vào file JSON
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    csv_file = 'data\\data.csv'     # Đường dẫn tới file CSV nguồn
    json_file = 'data\\data.json'   # Đường dẫn tới file JSON đích
    csv_to_json(csv_file, json_file)
    print(f"Đã chuyển đổi {csv_file} thành {json_file} thành công!")
