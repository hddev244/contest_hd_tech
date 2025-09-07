# Đọc input
nuoc_cam, so_coc = map(int, input().split())

# Tính lượng nước mỗi cốc
nuoc_moi_coc = nuoc_cam / so_coc

# In kết quả với 2 chữ số thập phân
print(f"{nuoc_moi_coc:.2f}")
