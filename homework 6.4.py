
lst = list(range(10))
for i in range(10):
    if i % 2 == 0:
        print(lst[i])
sum_of_digits = sum(i for i in range(10) if i % 2 == 0)
print(sum_of_digits)

