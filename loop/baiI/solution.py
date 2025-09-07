# Bài I: In ra các số chia hết cho 3 nhưng không chia hết cho 5 từ 1 đến 100
# Sử dụng vòng lặp for

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
