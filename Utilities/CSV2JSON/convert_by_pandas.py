# Convert CSV to JSON by Pandas
import pandas as pd

def csv_to_json_pandas(csv_file_path, json_file_path):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(csv_file_path)

    # Chuyển đổi DataFrame thành JSON và lưu vào file
    df.to_json(json_file_path, orient='records', force_ascii=False, indent=4)

if __name__ == "__main__":
    csv_file = 'data\\data.csv'     # Đường dẫn tới file CSV nguồn
    json_file = 'data\\data_pandas.json'   # Đường dẫn tới file JSON đích
    csv_to_json_pandas(csv_file, json_file)
    print(f"Đã chuyển đổi {csv_file} thành {json_file} thành công bằng pandas!")
