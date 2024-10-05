def func(ways, d, v, time=0, visited=set()):
    if d == v:
        return time

    visited.add(d)
    min_time = float('inf')

    for trip in ways[d]:
        t_depart, next_village, t_arrive = trip
        if time <= t_depart and next_village not in visited: 
            result_time = func(ways, next_village, v, t_arrive, visited)
            if result_time < min_time:
                min_time = result_time

    visited.remove(d)
    
    return min_time

def main():
    with open("input.txt", "r") as file:
        N = int(file.readline())
        d, v = map(int, file.readline().split())
        ways = {i+1: [] for i in range(N)}
        for i in range(int(file.readline())):
            a1, t1, a2, t2 = map(int, file.readline().split())
            ways[a1].append((t1, a2, t2))

    result = func(ways, d, v)

    with open("output.txt", "w") as file:
        if result == float('inf'):
            result = -1
        file.write(str(result))

if __name__ == "__main__":
    main()