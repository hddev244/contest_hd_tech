# Đọc input
a, b = map(int, input().split())

# Kiểm tra chia hết
if a % b == 0:
    print("a chia hết cho b")
else:
    print("a không chia hết cho b")
