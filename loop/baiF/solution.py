# Nhập số n
n = int(input())

# Tính giai thừa bằng vòng lặp for
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i

print(giai_thua)
