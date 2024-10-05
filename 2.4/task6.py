def func(string):
    n = len(string)
    Z = [0] * n
    
    for i in range(n):
        for j in range(i, n):
            if string[j] == string[j - i]:
                Z[i] += 1
            else:
                break
    
    return Z

def main():
    with open('input.txt') as file:
        string = file.readline().strip()

    result = func(string)

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, result[1:])))

if __name__ == "__main__":
    main()
