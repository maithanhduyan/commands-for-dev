# Odoo backup

- Sử dụng lệnh sau để build image:
> docker build -t odoo-backup .

- Sau khi build thành công, sử dụng lệnh sau để chạy container:
> docker build -t odoo-backup .


- Để sử dụng docker-compose.yml này, bạn cần tạo một file Dockerfile và backup.py trong thư mục chứa file docker-compose.yml. Sau đó, bạn có thể sử dụng lệnh sau để build và chạy container:
> docker-compose up --build


### Test
- 1 Cài đặt virtualenv nếu chưa có: 
> pip install virtualenv
- 2 Tạo một thư mục mới để chứa môi trường ảo và chạy lệnh sau để tạo môi trường ảo::
~~~~
cd path/to/your/project
virtualenv venv

~~~~
- 3. Kích hoạt môi trường ảo:
venv\Scripts\activate

- 4. Cài đat các thư viện cần thiết:
> pip install -r requirements.txt

- 5. Copy file "backup.conf.sample" chỉnh lại thành file "backup.conf". Chỉnh cấu hình phù hợp với server odoo.

- 6. Chạy ứng dụng:
> python app.py

- 7. Tam dừng ứng dụng:
> ctrl+c

- 8. Thoát khỏi môi trường ảo:
> deactivate
