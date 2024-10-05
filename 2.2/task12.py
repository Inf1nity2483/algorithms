def calculate_balance(root, data, result=[]):
    if root == 0:
        return 0, 0

    left_height, _ = calculate_balance(data[root][1], data, result)
    right_height, _ = calculate_balance(data[root][2], data, result)  

    balance = right_height - left_height
    result.append(str(balance))

    return max(left_height, right_height) + 1, result  

def main():
    with open('input.txt') as file:
        N = int(file.readline())
        
        data = {}
        for i in range(N):
            node, l, r = map(int, file.readline().split())
            data[i+1] = (node, l, r)
        
    result = calculate_balance(1, data) 
    result[1].reverse()

    with open('output.txt', 'w') as file:
        file.write('\n'.join(result[1]) + '\n')

if __name__ == '__main__':
    main()
