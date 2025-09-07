# Bài M: Kiểm tra số nguyên tố
# Sử dụng vòng lặp for

n = int(input())

if n <= 1:
    print("NO")
elif n == 2:
    print("YES")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("YES")
    else:
        print("NO")
