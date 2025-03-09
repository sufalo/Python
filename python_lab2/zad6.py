def fibonacci_generator(n: int):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 10
fib_gen = fibonacci_generator(n)

for number in fib_gen:
    print(number)
