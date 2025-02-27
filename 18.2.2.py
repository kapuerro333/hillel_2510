


    class MyIterator:
        def __init__(self, n):
            self.n = n
            self.current = -2

        def __iter__(self):
            return self

        def __next__(self):
            self.current += 2
            if self.current > self.n:
                raise StopIteration
            return self.current


    n = 10
    my_iterator = MyIterator(n)

    for num in my_iterator:
        print(num)