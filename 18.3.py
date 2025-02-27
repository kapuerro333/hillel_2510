def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} з аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} повернулаcь з наступним результатом: {result}")
        return result
    return wrapper

@my_decorator
def check(a, b):
    return a + b

check(3, 9)


import functools
def exception_handler_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка у функції {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler_decorator
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))