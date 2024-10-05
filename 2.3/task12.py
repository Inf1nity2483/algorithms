def func(ways, colors):
    room = 1
    for i in colors:
        if i not in ways[room]:
            return "INCORRECT"
        room = ways[room][i]

    return room

def main():
    with open("input.txt", "r") as file:
        n, m = map(int, file.readline().split())
        ways = {i: {} for i in range(1, n+1)}
        for i in range(m):
            u, v, c = map(int, file.readline().split())
            ways[u][c] = v
            ways[v][c] = u

        file.readline()

        colors = list(map(int, file.readline().split()))

    result = func(ways, colors)

    with open("output.txt", "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    main()