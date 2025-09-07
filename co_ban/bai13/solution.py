# Đọc input
so_sach, suc_chua_ke = map(int, input().split())

# Tính số sách còn dư (phép chia lấy dư)
so_sach_du = so_sach % suc_chua_ke

# In kết quả
print(so_sach_du)
