import unittest

car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

search_criteria = (2017, 1.6, 80000)

def filter_and_sort_cars(car_data, search_criteria):
    filtered_data = {
        car
        for car, details in car_data.items()
        if details[1] >= search_criteria[0] and details[2] >= search_criteria[1] and details[4] <= search_criteria[2]
    }

    sorted_cars = sorted(filtered_data, key=lambda car: car_data[car][4])
    return sorted_cars[:5]

first_cars = filter_and_sort_cars(car_data, search_criteria)

if first_cars:
    print("Авто знайдені:")
    for car in first_cars:
        print(f"Car: {car}, engine: {car_data[car][2]}, price: {car_data[car][4]}")
else:
    print("Авто не знайдено.")

class TestCarFilterFunction(unittest.TestCase):
    def test_car_count(self):
        test_cars = filter_and_sort_cars(car_data, search_criteria)
        self.assertEqual(len(test_cars), 5, "Number should be 5")

    def test_min_price(self):
      test_cars = filter_and_sort_cars(car_data, search_criteria)
      for car in test_cars:
        self.assertGreaterEqual(car_data[car][4], 25000, f"Price {car} should not be less than 25000")

    def test_engine_size(self):
      test_cars = filter_and_sort_cars(car_data, search_criteria)
      for car in test_cars:
        self.assertGreaterEqual(car_data[car][2], 1.6 , f"Engine size {car} should be not less than 1.6.")
if __name__ == '__main__':
    unittest.main()