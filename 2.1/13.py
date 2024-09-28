list1 = []
data = {}

def func(sum1, sum2, sum3, i):
    if sum([sum1, sum2, sum3]) == sum(list1):
        if sum1 == sum2 == sum3:
            return 1
        return 0
    
    b = (sum1, sum2, sum3)
    
    if b in data:
        return data[b]
    
    result = max(
        func(sum1 + list1[i], sum2, sum3, i+1),
        func(sum1, sum2 + list1[i], sum3, i+1),
        func(sum1, sum2, sum3 + list1[i], i+1)
    )

    data[b] = result

    return result


def main():
    global list1, data
    with open('input.txt') as file:
        n = int(file.readline())
        list1 = list(map(int, file.readline().split()))

    with open("output.txt", "w") as file:
        if sum(list1) % 3 == 0:
            file.write(str(func(0, 0, 0, 0)))
        else:
            file.write('0')