# Bài 3: Nhập vào bán kính hình tròn, in ra chu vi và diện tích (làm tròn 2 chữ số thập phân).

import math

# Đọc dữ liệu đầu vào
ban_kinh = float(input())

# Tính toán
chu_vi = 2 * math.pi * ban_kinh
dien_tich = math.pi * ban_kinh * ban_kinh

# In kết quả (làm tròn 2 chữ số thập phân)
print(f"Chu vi: {chu_vi:.2f}")
print(f"Diện tích: {dien_tich:.2f}")
