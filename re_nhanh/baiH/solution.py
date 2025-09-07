# Đọc input
nam = int(input())

# Kiểm tra năm nhuận
if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")
