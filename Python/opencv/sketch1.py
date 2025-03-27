# Description: Chuyển ảnh màu sang ảnh bút chì
"""
1. Sử dụng kỹ thuật “Pencil Sketch” (chia độ sáng)
Một phương pháp thường được gọi là “pencil sketch” có thể cho kết quả trực quan giống tranh chì hơn so với việc chỉ dùng Canny. 
Bạn có thể tham khảo đoạn mã dưới đây:
"""
import cv2
import numpy as np

# Đọc ảnh gốc
img = cv2.imread('images/original.jpg')
if img is None:
    print("Không thể đọc ảnh. Kiểm tra lại đường dẫn hoặc tên file.")
    exit()

# Chuyển sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Đảo ngược màu xám
inverted = 255 - gray

# Làm mờ ảnh đảo ngược (tăng kích thước kernel nếu cần làm mịn hơn)
blur = cv2.GaussianBlur(inverted, (21, 21), 0)

# Đảo ngược lại lần nữa
inverted_blur = 255 - blur

# Kết hợp ảnh xám và ảnh mờ đảo ngược theo công thức chia
pencil_sketch = cv2.divide(gray, inverted_blur, scale=256)

# Lưu ảnh kết quả
cv2.imwrite('images/pencil_sketch.jpg', pencil_sketch)
print("Đã lưu ảnh pencil_sketch.jpg")
