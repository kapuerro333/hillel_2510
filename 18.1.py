def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def fib_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


gen = even_numbers_generator(10)
print(next(gen))
print(next(gen))
print(next(gen))

gen_fib = fib_generator(100)
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))