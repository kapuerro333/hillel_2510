class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # Починаємо з останнього елемента

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


numbers = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(numbers)

for num in reverse_iter:
    print(num)