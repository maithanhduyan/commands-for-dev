Dưới đây là hướng dẫn thiết lập một máy chủ Git cơ bản trên Ubuntu 24.04 (tương tự cho các phiên bản Ubuntu khác). Môi trường được giả định là máy chủ (server) chạy Ubuntu 24.04 sạch, và bạn có quyền quản trị (root) để cài đặt và cấu hình.

---

## 1. Cập nhật hệ thống

Trước tiên, bạn nên cập nhật các gói và nâng cấp hệ thống:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 2. Cài đặt Git

Để cài đặt Git trên Ubuntu:

```bash
sudo apt install git -y
```

Kiểm tra phiên bản đã cài đặt:

```bash
git --version
```

---

## 3. Tạo tài khoản dành riêng cho Git

Để thuận tiện quản lý và tránh nhầm lẫn với tài khoản quản trị hệ thống, ta thường tạo một tài khoản riêng chuyên để lưu trữ code. Ví dụ, tạo user tên là `git`:

```bash
sudo adduser --disabled-password --gecos "" git
```

Giải thích:
- `--disabled-password` có nghĩa là người dùng này không có mật khẩu đăng nhập trực tiếp (nếu cần, bạn vẫn có thể đặt mật khẩu hoặc sử dụng SSH Key).
- `--gecos ""` bỏ qua các thông tin hỏi thêm (tên, số điện thoại...).

Sau khi tạo user `git`, bạn nên thiết lập SSH key cho tài khoản này nhằm bảo mật (thay vì sử dụng mật khẩu). 

---

## 4. Thiết lập SSH Key (từ máy trạm/laptop)

### 4.1 Tạo cặp SSH Key trên máy trạm (client)

Trên máy trạm (Windows/macOS/Linux), mở terminal/PowerShell và gõ:

```bash
ssh-keygen -t rsa -b 4096
```

- Thông thường, key sẽ được lưu vào `~/.ssh/id_rsa` (private key) và `~/.ssh/id_rsa.pub` (public key).
- Bạn có thể đặt passphrase hoặc để trống (tùy nhu cầu bảo mật).

### 4.2 Chép public key lên máy chủ Git

Giả sử IP hoặc tên miền của máy chủ Git là `gitserver.example.com`. Ta dùng lệnh (thay bằng đường dẫn và user của bạn):

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub git@gitserver.example.com
```

Hoặc bạn có thể thủ công copy nội dung file `id_rsa.pub` dán vào file `~/.ssh/authorized_keys` trên máy chủ, cụ thể:

1. Mở file `id_rsa.pub` trên máy trạm và copy toàn bộ nội dung.
2. SSH vào máy chủ và đăng nhập user `git`:
   ```bash
   ssh git@gitserver.example.com
   ```
3. Tạo (hoặc mở) file `~/.ssh/authorized_keys`:
   ```bash
   nano ~/.ssh/authorized_keys
   ```
4. Dán nội dung public key vào file, lưu và thoát. 
5. Phân quyền phù hợp:
   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/authorized_keys
   ```

---

## 5. Tạo kho lưu trữ (repository) “bare”

Để dùng máy chủ như một Git server, ta cần tạo một kho “bare” (không chứa code, chỉ chứa metadata của Git). Ví dụ, ta tạo một repo tên `project.git`:

```bash
# Đăng nhập vào máy chủ bằng user git
ssh git@gitserver.example.com

# Tạo thư mục chứa repo
mkdir -p ~/repositories
cd repositories

# Tạo repo “bare”
git init --bare project.git
```

Kho `bare` không dùng để làm việc trực tiếp, chỉ dùng để lưu trữ trung tâm. Mỗi lập trình viên sẽ clone repo này về để làm việc.

---

## 6. Phân quyền thư mục (nếu cần)

Thường thì owner của thư mục `project.git` sẽ là user `git`. Kiểm tra lại:

```bash
ls -l ~/repositories
```

Nếu cần, bạn có thể chỉnh sửa quyền. Thông thường, nếu tất cả đều dùng chung user `git` qua SSH key thì phân quyền mặc định là đủ. 

---

## 7. Thiết lập firewall (tùy chọn)

Nếu máy chủ của bạn nằm sau firewall hoặc có iptables/ufw, hãy đảm bảo cổng SSH (mặc định 22) được mở. Ví dụ:

```bash
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
```

Bạn cũng có thể thay đổi cổng SSH (việc này cần cẩn thận, tránh tự khoá chính mình). Để đổi cổng SSH, sửa file `/etc/ssh/sshd_config` và đặt `Port <cổng_mới>` rồi khởi động lại dịch vụ SSH:

```bash
sudo nano /etc/ssh/sshd_config
sudo systemctl restart ssh
```

---

## 8. Sử dụng repo từ máy trạm

Trên máy trạm, để clone repo `project.git`:

```bash
git clone git@gitserver.example.com:repositories/project.git
```

Hoặc:

```bash
git clone ssh://git@gitserver.example.com/~/repositories/project.git
```

Tuỳ theo cấu trúc thư mục trên máy chủ bạn đặt thế nào. Sau đó, lập trình viên có thể thực hiện commit, push, pull như các repo Git bình thường.

---

## 9. Quản lý nhiều repository

Để quản lý nhiều repo trên cùng máy chủ, bạn có thể:
- Tạo các repo “bare” tương tự tại `~/repositories/ten_project_1.git`, `~/repositories/ten_project_2.git`, ...
- Hoặc phân chia quyền truy cập cho từng repo nếu cần (tạo group, phân quyền cho user, v.v.).

Nếu công ty có nhu cầu phức tạp hơn (quản lý giao diện web, issue, CI/CD…), bạn có thể cân nhắc cài đặt các nền tảng quản lý Git như **GitLab**, **Gitea** hoặc **GitHub Enterprise** (tuỳ mô hình, chi phí và nhu cầu).

---

## 10. Một số lưu ý bảo mật và tối ưu

1. **Bắt buộc dùng SSH key** thay vì mật khẩu cho user `git`.
2. **Đổi cổng SSH** (không để mặc định 22) nếu cần tăng cường bảo mật, kèm cấu hình firewall.
3. **Bật tường lửa ufw** và chỉ mở cổng cần thiết.
4. **Theo dõi log**: Sử dụng `journalctl -u ssh` hoặc `cat /var/log/auth.log` để kiểm tra đăng nhập SSH.
5. **Sao lưu định kỳ** các “bare” repo hoặc toàn bộ thư mục `~/repositories`.
6. **Nâng cấp định kỳ** hệ thống, nhất là các gói bảo mật.

---

## 11. Tóm tắt

1. **Cập nhật hệ thống**: `sudo apt update && sudo apt upgrade -y`.
2. **Cài Git**: `sudo apt install git -y`.
3. **Tạo user `git`**: `sudo adduser --disabled-password --gecos "" git`.
4. **Thiết lập SSH key**: Từ máy trạm, tạo key rồi chép public key lên máy chủ (file `~/.ssh/authorized_keys`).
5. **Tạo repo “bare”**: `git init --bare project.git`.
6. **Clone từ máy trạm**: `git clone git@gitserver.example.com:repositories/project.git`.
7. **Push/Pull/Commit** như bình thường.

Vậy là bạn đã có một **Git server** đơn giản trên Ubuntu 24.04 để mọi người cùng làm việc. Nếu quy mô công ty cần giao diện web, issue tracking, CI/CD… thì hãy cân nhắc các giải pháp nâng cao như GitLab, Gitea, hoặc các nền tảng quản lý mã nguồn chuyên nghiệp khác. Chúc bạn triển khai thành công!