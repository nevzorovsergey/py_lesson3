import random

SIZE = 10
numbers = [random.randint(-SIZE, SIZE) for _ in range(SIZE)]
print(numbers)

maxindex = 0
maxnumber = 0
for i in range(len(numbers)):
    if numbers[i] < 0:
        maxindex = i
        maxnumber = numbers[i]
        break
for ii in range(i,len(numbers)):
    if numbers[ii] < 0 and maxnumber < numbers[ii]:
        maxindex = ii
        maxnumber = numbers[ii]

print(f'Самое больше отрицательное число {maxnumber} в позиции {maxindex} ')
