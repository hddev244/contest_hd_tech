# Bài K: Vẽ tam giác vuông bằng dấu *
# Sử dụng vòng lặp for

n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
