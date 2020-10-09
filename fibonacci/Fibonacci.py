def fibonacci(num):
    if num == 1:
        print(0)
        return
    if num == 2:
        print(0)
        print(1)
    a, b = 0, 1
    for i in range(3, num + 1):
        c = a + b
        print(c)
        a, b = b, c
