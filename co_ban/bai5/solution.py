# Bài 5: Nhập vào một chuỗi ký tự, in ra chuỗi đó viết hoa và viết thường.

# Đọc dữ liệu đầu vào
chuoi = input().strip()

# Chuyển đổi
viet_hoa = chuoi.upper()
viet_thuong = chuoi.lower()

# In kết quả
print(f"Viết hoa: {viet_hoa}")
print(f"Viết thường: {viet_thuong}")
