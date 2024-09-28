from copy import deepcopy
n = 0
min_price = float('inf')
data = [0, 0]
history = []


def func(full_price, tickets, i, all_tickets, hs=[]):
    if i == n:
        global min_price, data, history
        if full_price < min_price or (full_price == min_price and tickets > data[0]):
            min_price = full_price
            data = [tickets, all_tickets]
            history = hs
        return full_price
    k = float('inf')
    if list1[i] > 100:
        g = func(full_price+list1[i], tickets+1, i+1, all_tickets+1, deepcopy(hs))
    else:
        g = func(full_price+list1[i], tickets, i+1, all_tickets, deepcopy(hs))
    if tickets > 0:
        hs.append(i+1)
        k = func(full_price, tickets-1, i+1, all_tickets, deepcopy(hs))
    return min([k, g])


def main():
    global list1, n, min_price, data
    with open('input.txt') as file:
        n = int(file.readline())
        list1 = list(map(int, file.readlines()))

    with open("output.txt", "w") as file:
        file.write(str(func(0, 0, 0, 0))+'\n')
        file.write(' '.join(map(str, data))+'\n')
        file.write('\n'.join(map(str, history)))
