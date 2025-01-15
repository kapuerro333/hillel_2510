import csv
from pathlib import Path

file_path1 = r'C:\Users\BestLaptop\hillel_2510\lesson 03\random.csv'
file_path2 = r'C:\Users\BestLaptop\hillel_2510\lesson 03\random-michaels.csv'

# reading the 1st file
with open(file_path1, 'r', encoding='utf-8') as file1:
    reader1 = csv.reader(file1)
    file1_lines = [row for row in reader1]

# reading the 2nd file
with open(file_path2, 'r', encoding='utf-8') as file2:
    reader2 = csv.reader(file2)
    file2_lines = [row for row in reader2]

# Об'єднуємо всі рядки
all_lines = file1_lines + file2_lines

unique_lines = []
seen = set()

for line in all_lines:
    stripped_line = tuple(val.strip().lower() for val in line)
    if stripped_line not in seen:
        unique_lines.append(line)
        seen.add(stripped_line)

output_file_path = r'C:\Users\BestLaptop\result_Moskalchuk.csv'

try:
    with open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(unique_lines)
    print("Файл успішно створено!")
except Exception as e:
    print(f"Помилка при записі файлу: {e}")

# Обчислюємо загальну кількість рядків та кількість унікальних
total_lines = len(file1_lines) + len(file2_lines)
unique_lines_count = len(unique_lines)

print(f"Загальна кількість рядків: {total_lines}")
print(f"Кількість рядків у файлі: {unique_lines_count}")

# Перевірка, чи були дублікати
if total_lines != unique_lines_count:
    print("Є дублікати, які були видалені!")
else:
    print("Дублікати відсутні.")