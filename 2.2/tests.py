import random

def generate_test(n):
    commands = []
    existing_elements = set()
    
    for _ in range(n):
        if len(existing_elements) > 0 and random.random() < 0.33:  # 33% вероятность выбора удаления или поиска
            command_type = random.choice([0, -1])
        else:
            command_type = 1  # Всегда добавлять, если список пуст

        if command_type == 1:  # Добавить элемент
            # Генерируем уникальный ключ
            while True:
                key = random.randint(-10**9, 10**9)
                if key not in existing_elements:
                    existing_elements.add(key)
                    break
            commands.append(f"1 {key}")
        
        elif command_type == 0:  # Найти k-й максимум
            # Запрашиваем k-й максимум, только если в наборе есть элементы
            if existing_elements:
                k = random.randint(1, len(existing_elements))
                commands.append(f"0 {k}")

        elif command_type == -1:  # Удалить элемент
            # Удаляем случайный существующий ключ
            if existing_elements:  # Убедимся, что есть элементы для удаления
                key_to_remove = random.choice(list(existing_elements))
                existing_elements.remove(key_to_remove)
                commands.append(f"-1 {key_to_remove}")

    return commands

def main():
    n = random.randint(100000)
    commands = generate_test(n)

    with open('input.txt', 'w') as f:
        f.write(f"{n}\n")
        for command in commands:
            f.write(command + "\n")

if __name__ == "__main__":
    main()
