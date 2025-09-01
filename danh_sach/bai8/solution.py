# Bài 8: Nhập và in danh sách

# Đọc số lượng phần tử
n = int(input())

# Tạo danh sách rỗng
numbers = []

# Nhập n số vào danh sách
for i in range(n):
    so = int(input())
    numbers.append(so)

# In danh sách trên một dòng, cách nhau bởi khoảng trắng
print(*numbers)
