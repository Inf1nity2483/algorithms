def func(substring, string):
    result = []
    for i in range(len(string)):
        new_substring = string[i:len(substring)+i]
        if new_substring == substring:
            result.append(i+1)

    return str(len(result)), ' '.join(map(str, result))

def main():
    with open('input.txt') as file:
        substring = file.readline().strip()
        string = file.readline().strip()

    result = func(substring, string)

    with open('output.txt', 'w') as file:
        file.write(result[0]+'\n')
        file.write(result[1])


if __name__ == "__main__":
    main()