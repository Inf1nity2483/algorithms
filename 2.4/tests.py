import random
import string

def generate_random_string(length):
    """Генерирует случайную строку заданной длины из маленьких латинских букв."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def write_test_case_to_file(filename):
    """Записывает сгенерированный тестовый случай в указанный файл."""
    length = random.randint(2, 10**6)  # Длина строки от 2 до 10^6
    s = generate_random_string(length)
    with open(filename, 'w') as f:
        f.write(s + '\n')

def main():
    write_test_case_to_file('input.txt')
    print('Сгенерирован один тест в файле input.txt.')

if __name__ == "__main__":
    main()
