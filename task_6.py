import random

SIZE = 10
numbers = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(numbers)

minnumber = numbers[0]
minindex = 0
maxnumber = 0
maxindex = 0
for i in range(len(numbers)):
    if numbers[i] > maxnumber:
        maxnumber = numbers[i]
        maxindex = i
    if numbers[i] < minnumber:
        minnumber = numbers[i]
        minindex = i

if minindex > maxindex:
    start = maxindex
    finish = minindex
else:
    start = minindex
    finish = maxindex

result = 0
for i in range(start+1, finish):
    result += numbers[i]

print(f'Максимальное чило {maxnumber} в позиции {maxindex}')
print(f'Минимальное чило {minnumber} в позиции {minindex}')
print(f'Сумма между {result}')