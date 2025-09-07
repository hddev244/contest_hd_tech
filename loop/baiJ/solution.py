# Bài J: In ra dãy Fibonacci đến số thứ n
# Sử dụng vòng lặp while

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(1)
else:
    print(1)
    print(1)
    
    a, b = 1, 1
    count = 3
    
    while count <= n:
        next_fib = a + b
        print(next_fib)
        a, b = b, next_fib
        count += 1
