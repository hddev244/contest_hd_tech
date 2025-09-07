# Đọc input
a, b = map(int, input().split())

# So sánh và in kết quả
if a > b:
    print("a lớn hơn b")
elif b > a:
    print("b lớn hơn a")
else:
    print("a bằng b")
