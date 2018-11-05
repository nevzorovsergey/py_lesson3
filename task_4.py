import random

SIZE = 100
numbers = [random.randint(0, SIZE) for _ in range(SIZE)]
print(numbers)

maxcount = 0
maxnumber = 0
for i in range(len(numbers)):
    count = 0
    for ii in range(i, len(numbers)):
        if numbers[i] == numbers[ii]:
            count += 1
    if maxcount < count:
        maxcount = count
        maxnumber = numbers[i]

print(f'Число {maxnumber} встречается {maxcount} раз ')
