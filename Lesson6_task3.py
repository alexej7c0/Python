a = int(input('Введите число "А" '))
b = int(input('Введите число "B" '))
count = 0
for i in range(a, b + 1):
    if i != 0 and i % 2 == 0:
        count += 1
print(f'Чётных чисел: {count}')
