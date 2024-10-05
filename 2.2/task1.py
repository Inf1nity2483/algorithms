def postorder(root, data, result=[]):
    if data[root][1] != -1:
        postorder(data[root][1], data, result)

    if data[root][2] != -1:
        postorder(data[root][2], data, result) 

    result.append(str(data[root][0]))

    return result

def preorder(root, data, result=[]):
    result.append(str(data[root][0]))

    if data[root][1] != -1:
        preorder(data[root][1], data, result)

    if data[root][2] != -1:
        preorder(data[root][2], data, result) 

    return result

def inorder(root, data, result=[]):
    if data[root][1] != -1:
        inorder(data[root][1], data, result)

    result.append(str(data[root][0]))

    if data[root][2] != -1:
        inorder(data[root][2], data, result) 

    return result

def main():
    with open('input.txt') as file:
        N = int(file.readline())
        data = []
        for i in range(N):
            node, l, r = map(int, file.readline().split())
            data.append((node, l, r))

    result_inorder = inorder(0, data)
    result_preorder = preorder(0, data)
    result_postorder = postorder(0, data)

    with open('output.txt', 'w') as file:
        file.write(' '.join(result_inorder)+'\n')
        file.write(' '.join(result_preorder)+'\n')
        file.write(' '.join(result_postorder)+'\n')




if __name__ == '__main__':
    main()
