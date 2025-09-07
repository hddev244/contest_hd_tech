# Nhập số n
n = int(input())

# Đếm chữ số bằng vòng lặp while
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10

print(count)
