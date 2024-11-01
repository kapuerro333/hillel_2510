# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("World!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
x = apples * 4
banana = x
print(x)
# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4
# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
garden_apples = 4
garden_pear = garden_apples + 5
garden_plum = garden_apples - 2
garden_trees = garden_apples + garden_pear + garden_plum
print("У саду посадили", garden_apples, "яблук,", garden_pear, "груш, на 5 більше ніж яблук,",
      garden_plum, "слив, на 2 менше ніж яблук.")
print("Отже, посадили", garden_trees, "дерев.")
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_indicator = 0
before_meal = temperature_indicator + 5
after_meal = before_meal - 10
evening_temperature = after_meal + 4

print("До обіду", before_meal, "була на 5 градусів вище нуля,",
      "після обіду", after_meal, "температура опустилася на 10 градусів,",
      "Надвечір", evening_temperature, "потепліло на 4 градуси.")
print("Підсумуємо, що температура надвечір =", evening_temperature)
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_actors = 24
girls_actors = boys_actors//2
today_boys = boys_actors - 1
today_girls = girls_actors - 2
today_actors = today_boys + today_girls

print("Загалом у театральному гуртку хлопчиків =", boys_actors,
      ", дівчаток =", girls_actors, "вдвічі менше,",
      "1 хлопчик захворів,", today_boys, "хлопчиків,",
      "а 2 дівчинки не прийшли сьогодні,", today_girls, "дівчаток.")

print("Підсумуємо, що загалом прийшло =", today_actors)
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book)/2
order = first_book + second_book + third_book
print("Перша книга коштує:", first_book, "грн,",
      "Друга книга коштує на 2 грн дорожче:", second_book, "грн,",
      "Третя книга - половина вартості першої та другої разом:", third_book, "грн.",
      "Загальна вартість:", order, "грн.")

print("Підсумуємо, що загалом прийшло =", order, "грн")
