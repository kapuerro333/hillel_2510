import json
import logging

# Шляхи до файлів
file_path1 = r'C:\Users\BestLaptop\hillel_2510\lesson 03\localizations_en.json'
file_path2 = r'C:\Users\BestLaptop\hillel_2510\lesson 03\localizations_ru.json'
file_path3 = r'C:\Users\BestLaptop\hillel_2510\lesson 03\login.json'
file_path4 = r'C:\Users\BestLaptop\hillel_2510\lesson 03\swagger.json'

# Функція для перевірки валідності JSON
def is_valid_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True
    except json.JSONDecodeError as e:
        logger.error(f"Помилка в JSON в файлі {file_path}: {e}")
        return False
    except Exception as e:
        logger.error(f"Сталася помилка при читанні файлу {file_path}: {e}")
        return False

# Налаштування логування
logging.basicConfig(
    filename='json__Yurii.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()


file_paths = [file_path1, file_path2, file_path3, file_path4]

# Перевірка кожного файлу
for path in file_paths:
    if is_valid_json(path):
        print(f"{path} — JSON є валідним!")
    else:
        print(f"{path} — JSON не є валідним.")