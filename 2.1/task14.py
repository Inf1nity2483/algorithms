def func(expr):
    n = (len(expr) // 2) + 1
    MVal = [[-float('inf')] * n for _ in range(n)]
    mVal = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        MVal[i][i] = mVal[i][i] = int(expr[2 * i])
    
    for l in range(2, n + 1):  
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                op = expr[2 * k + 1]
                if op == '-':
                    MVal[i][j] = max(MVal[i][j], eval(f"MVal[i][k] {op} mVal[k + 1][j]"))
                    mVal[i][j] = min(mVal[i][j], eval(f"mVal[i][k] {op} MVal[k + 1][j]"))
                else:
                    MVal[i][j] = max(MVal[i][j], eval(f"MVal[i][k] {op} MVal[k + 1][j]"))
                    mVal[i][j] = min(mVal[i][j], eval(f"mVal[i][k] {op} mVal[k + 1][j]"))                    

    return MVal[0][n - 1]


def main():
    with open('input.txt') as file:
        expr = file.readline()
        
    if expr:
        with open("output.txt", "w") as file:
            file.write(str(func(expr)))