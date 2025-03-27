"""
2. Dò cạnh Canny kèm tiền xử lý và hậu xử lý
Nếu bạn muốn giữ phong cách line art (chỉ đường viền) nhưng không bị nhiễu, hãy kết hợp các bước:

Chuyển sang ảnh xám.

Giảm nhiễu bằng Gaussian Blur (hoặc Bilateral Filter) trước khi chạy Canny.

Chọn ngưỡng Canny phù hợp (ví dụ (50, 150), (100, 200),...).

Xử lý hình thái (Morphological) để xóa các đốm nhiễu li ti (mở/đóng ảnh - cv2.morphologyEx).

"""

import cv2
import numpy as np

# Đọc ảnh gốc
img = cv2.imread('images/original.jpg')
if img is None:
    print("Không thể đọc ảnh.")
    exit()

# 1) Chuyển sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2) Giảm nhiễu bằng GaussianBlur
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# 3) Dò cạnh Canny
edges = cv2.Canny(gray, 50, 150)

# 4) Xử lý hình thái để làm gọn nét
#    - Dùng phép 'dilate' rồi 'erode' (hoặc ngược lại) để bớt nhiễu
kernel = np.ones((3,3), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)
edges = cv2.erode(edges, kernel, iterations=1)

# Đảo màu để đường viền thành trắng, nền thành đen
inverted_edges = cv2.bitwise_not(edges)

# Lưu ảnh kết quả
cv2.imwrite('images/line_art.jpg', inverted_edges)
print("Đã lưu ảnh line_art.jpg")
