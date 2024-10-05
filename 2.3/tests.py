import random

def generate_test():
    # Количество деревень (1 ≤ N ≤ 100)
    N = 100
    
    # Выбор начальной и конечной деревни
    d = random.randint(1, N)
    v = random.randint(1, N)
    
    # Количество автобусных рейсов (0 ≤ R ≤ 10000)
    R = random.randint(0, 10000)
    
    # Список рейсов
    trips = []
    for _ in range(R):
        # Рейсы могут быть из любого города в любой другой, с заданными временами
        departure_village = random.randint(1, N)
        departure_time = random.randint(0, 10000)
        arrival_village = random.randint(1, N)
        arrival_time = random.randint(departure_time + 1, 10000)  # время прибытия должно быть после времени отправления
        
        # Добавляем рейс в список
        trips.append((departure_village, departure_time, arrival_village, arrival_time))
    
    # Форматируем результат в виде строк
    result = []
    result.append(f"{N}")
    result.append(f"{d} {v}")
    result.append(f"{R}")
    
    for trip in trips:
        result.append(" ".join(map(str, trip)))

    return "\n".join(result)

# Генерация теста
test_case = generate_test()

# Запись в файл input.txt
with open("input.txt", "w") as f:
    f.write(test_case)

print("Тестовый случай сохранен в файл input.txt.")
