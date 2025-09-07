# Đọc input
a, b = map(int, input().split())

# Tính tổng và tích
tong = a + b
tich = a * b

# So sánh
if tong > tich:
    print("Tổng lớn hơn")
else:
    print("Tích lớn hơn hoặc bằng")
