def func(n, arr):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] + arr[j + 1] < arr[j + 1] + arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return "".join(arr)

def main():
    with open("input.txt", "r") as file:
        n = int(file.readline())
        arr = list(file.readline().split())

    with open("output.txt", "w") as file:
        file.write(str(func(n, arr)))