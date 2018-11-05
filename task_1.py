for i in range(2, 10):
    count = 0
    for natural in range(2, 100):
        if natural % i == 0:
            count += 1
    print(f'Число {i} кратно {count} чисел')
