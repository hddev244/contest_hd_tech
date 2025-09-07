# Bài L: Đảo ngược một số nguyên
# Sử dụng vòng lặp while

n = int(input())

reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10

print(reversed_num)
