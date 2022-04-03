from random import randrange

# Integer from 0 to 9 inclusive
result = []

for idx in range(3):
    tem = []
    for idx in range(5):
        tem.append(randrange(100))
    result.append(tem)
    print(result)