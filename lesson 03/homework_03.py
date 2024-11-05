alice_in_wonderland2 = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where," said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland2 = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
# task 03 == Виведіть змінну alice_in_wonderland на друк
print (alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_blackSea = 436402
area_azov_sea = 37800
sum_area = area_blackSea + area_azov_sea
print ("Площа Чорного та Азовського морів =",sum_area, "km2")
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""


sum_total = 375291
x_and_y = 250449
y_and_z = 222950

z = sum_total - x_and_y
x = sum_total - y_and_z
y = y_and_z - z

print ("Отже, маєму таку кількість товару на кожному складі =", x,"перший склад", y,"другий склад", z,"третій склад")
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
number_payments_months = 18
sum_in_month = 1179
total_price = sum_in_month * number_payments_months
print("Загальна вартість компютера =" , total_price,"грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
remainder_a = 8019 % 8
print ("Остача від ділення =", remainder_a)
remainder_b = 9907 % 9
print ("Остача від ділення =", remainder_b)
remainder_c = 2789 % 5
print ("Остача від ділення =", remainder_c)
remainder_d = 7248 % 6
print ("Остача від ділення =", remainder_d)
remainder_e = 7128 % 5
print ("Остача від ділення =", remainder_e)
remainder_f = 19224 % 9
print ("Остача від ділення =", remainder_f)
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
sum_money = pizza_big + pizza_medium + juice + cake + water
print ("Загальна сума замовлення = ",sum_money, "грн.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos= 232
photo_per_page= 8
all_photos_per_pages=all_photos//photo_per_page
print ("Кількість сторінок знадобиться Ігорю, щоб вклеїти всі фото =", all_photos_per_pages)
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
petrol_litre_100km = 9
fuel_tank=48
#Рішення на 1 питання
petrol_per_distance = total_distance * petrol_litre_100km/100
print ("Кількість літрів бензину для подорожі=",petrol_per_distance)
#Рішення на 2 питання
#Поділимо загальну кількість палива, необхідного для подорожі на об*єм паливного баку.
station_stop = (petrol_per_distance + fuel_tank - 1) // fuel_tank
print("Кількість зупинок на заправку =", int(station_stop))