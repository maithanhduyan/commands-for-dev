bật chế độ command line trên debian khi khởi động
ChatGPT
Để khởi động vào chế độ dòng lệnh (command line) thay vì vào môi trường đồ họa (GUI) trên Debian, bạn có thể thực hiện các bước sau:

Mở tập tin cấu hình grub để chỉnh sửa:

~~~~
>sudo nano /etc/default/grub
~~~~
Tìm dòng bắt đầu bằng GRUB_CMDLINE_LINUX_DEFAULT và chỉnh sửa giá trị để thêm text vào cuối. Điều này sẽ bắt máy tính khởi động vào chế độ dòng lệnh.Ví dụ:

~~~~
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash text"
~~~~
Lưu tập tin cấu hình và thoát.

- Cập nhật grub để áp dụng thay đổi:
~~~~
sudo update-grub
sudo systemctl set-default multi-user.target
~~~~
- Khởi động lại máy tính:
~~~~
sudo reboot
~~~~

Khi máy tính khởi động lại, nó sẽ vào chế độ dòng lệnh thay vì môi trường đồ họa. Để trở lại môi trường đồ họa sau này, bạn có thể sử dụng lệnh startx.