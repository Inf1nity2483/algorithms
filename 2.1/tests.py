import random

with open('input.txt', 'w') as file:
    file.write(f'25\n')
    for i in range(25):
        file.write(f'{random.randint(0, 300)}\n')
    # file.write(''.join([str(random.randint(0, 9)) if i % 2 == 0 else random.choice(["+", '-', '*']) for i in range(29) ]))