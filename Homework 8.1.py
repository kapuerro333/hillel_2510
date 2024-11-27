my_array = ["1,2,3,4", "5,6,7,8", "qwerty1,2,3"]

def sum_numbers(list_of_strings):
    for string in list_of_strings:
        try:
            numbers = list(map(int, string.split(',')))
            general_sum = sum(numbers)
            print(general_sum)
        except ValueError:
            print("Не можу це зробити!")

sum_numbers(my_array)