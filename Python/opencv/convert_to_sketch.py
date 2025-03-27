import cv2
import numpy as np

# Đọc ảnh gốc
img = cv2.imread('images/bong_da_tre_em.jpg')

# Bước 1: Chuyển sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Bước 2: Dò cạnh (Edge Detection) - tham số 50, 150 chỉ là ví dụ
edges = cv2.Canny(gray, 50, 150)

# Bước 3: Đảo ngược màu cạnh để được nét vẽ trắng trên nền đen
inverted_edges = cv2.bitwise_not(edges)

# Lưu kết quả
cv2.imwrite('images/line_art.jpg', inverted_edges)
