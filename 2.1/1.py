def func(n, W, list):
    list.sort(key=lambda x: x[1], reverse=True)

    k = 0

    for i in list:
        if W < i[0]:
            k += W / i[0] * (i[1] * i[0])
            break

        k += i[0]*i[1]
        W -= i[0]

    return f'{k:.4f}'

def main():
    with open("input.txt", "r") as file:
        n, W = map(int, file.readline().split())
        list = []
        for i in range(n):
            p, w = map(int, file.readline().split())
            list.append((w, p/w))

    result = func(n, W, list)

    with open("output.txt", "w") as file:
        file.write(result)