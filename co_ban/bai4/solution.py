# Bài 4: Nhập vào chiều dài và chiều rộng hình chữ nhật, in ra chu vi và diện tích.

# Đọc dữ liệu đầu vào
chieu_dai = float(input())
chieu_rong = float(input())

# Tính toán
chu_vi = 2 * (chieu_dai + chieu_rong)
dien_tich = chieu_dai * chieu_rong

# Format số (loại bỏ .0 nếu là số nguyên)
chu_vi_str = f"{chu_vi:.1f}".rstrip('0').rstrip('.')
dien_tich_str = f"{dien_tich:.1f}".rstrip('0').rstrip('.')

# In kết quả
print(f"Chu vi: {chu_vi_str}")
print(f"Diện tích: {dien_tich_str}")
