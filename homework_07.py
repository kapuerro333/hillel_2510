# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
           break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
add = lambda x, y: x + y
print(add(3, 4))

def add(x, y):
    return x + y

print(add(3, 4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([3, 4, 5]))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hillel_IT"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(s):
    words = s.split()
    return max(words, key=len)
print(longest_word("Hillel_IT is a great place"))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def count_title_words(text):
    counter = 0
    for word in text.split():
        if word.istitle():
            counter += 1
    return counter

hillel_practice_best_option = "The show must go on"
print(count_title_words(hillel_practice_best_option))
# task 8
def find_second_occurrence(text, word):
    first_index = text.find(word)
    if first_index != -1:
        second_index = text.find(word, first_index + 1)
        if second_index != -1:
            return f"Знайдено 2 входження на позиції {second_index}."
        else:
            return "Підстрічка не знайдена для 2 входження."
    else:
        return "Підстрічка не знайдена для першого входження."

adventures_of_tom_sawyer = "Tom is a good friend of Tom. Tom loves adventures."
word = "Tom"
print(find_second_occurrence(adventures_of_tom_sawyer, word))
# task 9
def starts_with_phrase(text, phrase):
    sentences = text.split(".")

    filtered_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return any(sentence.startswith(phrase) for sentence in filtered_sentences)

adwentures_of_tom_sawer = """
By the time Tom had made up his mind, he felt that he was no longer a boy. 
He had to move fast to escape from the trouble he had gotten himself into.
By the time he reached the town, he knew things were about to change forever.
Tom wondered what would happen next.
"""
phrase = "By the time"
result = starts_with_phrase(adwentures_of_tom_sawer, phrase)
print(result)
# task 10
def count_symbols_in_last_sentence(text):
    sentences = text.split(".")
    filtered_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    if filtered_sentences:
        last_sentence = filtered_sentences[-1]
        return len(last_sentence)
    else:
        return 0

adwentures_of_tom_sawer = """
Tom was a clever boy. He liked adventures and was always looking for new ones. 
By the time he was ready, everyone had already left. He decided to follow them. 
The journey was long and tiring, but he did not give up.
"""

number_of_symbols = count_symbols_in_last_sentence(adwentures_of_tom_sawer)
print(number_of_symbols)
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
