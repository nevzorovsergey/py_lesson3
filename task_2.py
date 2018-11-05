import random

SIZE = 10
numbers = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(numbers)

evens = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens.append(i)

print('Индексы четных чисел массиве ', evens)

