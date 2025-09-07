# Bài O: Tìm bội số chung nhỏ nhất (BCNN) của 2 số
# Sử dụng vòng lặp while

a, b = map(int, input().split())

# Tìm BCNN bằng cách tăng dần từ max(a,b)
lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print(lcm)
