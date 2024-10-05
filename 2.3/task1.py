from copy import deepcopy

def func(U, V, ways):
    if V in ways[U] or U in ways[V]:
        return 1

    max_ = 0

    for i in ways[U]:
        new_ways = deepcopy(ways)
        new_ways[U].remove(i)
        new_ways[i].remove(U)
        max_ = max(func(i, V, new_ways), max_)

        if max_ == 1:
            return 1

    return max_

def main():
    with open("input.txt", "r") as file:
        n, m = map(int, file.readline().split())
        ways = {i: [] for i in range(1, n+1)}
        for i in range(m):
            u, v = map(int, file.readline().split())
            ways[u].append(v)
            ways[v].append(u)

        U, V = map(int, file.readline().split())

    result = func(U, V, ways)

    with open("output.txt", "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    main()