import random
for i in range(0, 5, 1):
    for j in range(0, 5, 1):
        if i == j:
            print(10)
        else:
            print(abs(1 - random.randrange(10) * round((i - j)) ** 2))
