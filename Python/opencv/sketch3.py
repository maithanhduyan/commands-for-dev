"""
3. Thử nghiệm với Adaptive Threshold (ngưỡng thích nghi)
Thay vì Canny, bạn cũng có thể dùng Adaptive Threshold để tách vùng sáng/tối và giữ lại vùng “viền” rõ ràng:
"""

import cv2

img = cv2.imread('images/original.jpg')
if img is None:
    print("Không thể đọc ảnh.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Giảm nhiễu
gray = cv2.GaussianBlur(gray, (3,3), 0)

# Ngưỡng thích nghi
thresh = cv2.adaptiveThreshold(gray, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 
                               11, 2)

cv2.imwrite('images/line_art_thresh.jpg', thresh)
print("Đã lưu ảnh line_art_thresh.jpg")
