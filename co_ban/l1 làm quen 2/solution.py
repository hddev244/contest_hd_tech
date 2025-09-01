# Đọc dữ liệu đầu vào
input_line = input().strip()

# Tách các thông tin từ chuỗi đầu vào
parts = input_line.split(", ")
ten = parts[0]
tuoi = parts[1]
dia_chi = parts[2]
so_dien_thoai = parts[3]

# In kết quả theo format yêu cầu
print(f"Xin chào, mình là {ten}, năm nay {tuoi} tuổi.")
print(f"Mình ở {dia_chi}. Số điện thoại của mình là: {so_dien_thoai}.")
