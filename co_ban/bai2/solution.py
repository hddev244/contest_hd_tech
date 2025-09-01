# Bài 2: Nhập vào 3 số nguyên, in ra tổng, hiệu, tích, thương của chúng.

# Đọc dữ liệu đầu vào
a = int(input())
b = int(input())
c = int(input())

# Tính toán
tong = a + b + c
hieu = a - b - c
tich = a * b * c
thuong = a / (b * c)

# In kết quả
print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương: {thuong:.2f}".rstrip('0').rstrip('.'))
