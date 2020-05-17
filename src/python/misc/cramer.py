n = 3
A = Matrix(n, n)
B = [PAdic("2", 5), PAdic("3", 5), PAdic("3", 5)]

for i in range(0, n, 1):
    row = []
    for j in range(0, n, 1):
        if i == j:
            row.append(PAdic("10", 5))
        else:
            number = round(1 - (i - j) ** 2 / n)
            row.append(PAdic(str(number), 5))
    A[i] = row
