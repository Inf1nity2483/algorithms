class Struct:
    def __init__(self) -> None:
        self.data = []

    def add(self, key: int) -> None:
        index = self.binary_search_insert_index(key)
        self.data.insert(index, key)

    def binary_search_insert_index(self, key: int) -> int:
        low, high = 0, len(self.data)
        while low < high:
            mid = (low + high) // 2
            if self.data[mid] < key: 
                low = mid + 1
            else:
                high = mid
        return low
    
    def remove(self, key: int):
        index = self.binary_search_insert_index(key)
        self.data.pop(index)

    def k(self, key: int):
        return str(self.data[-key])

def main():
    with open('input.txt') as file:
        N = int(file.readline())
        
        struct = Struct()
        result = []
        for _ in range(N):
            c, k = map(str, file.readline().split())
            k = int(k)
            if c in ['1', '+1']:
                struct.add(k)
            elif c == '-1':
                struct.remove(k)
            else:
                result.append(
                    struct.k(k)
                )


    with open('output.txt', 'w') as file:
        file.write('\n'.join(result) + '\n')

if __name__ == '__main__':
    main()
