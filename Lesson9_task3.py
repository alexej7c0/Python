seq = [int(i) for i in input('Введите ряд чисел через пробел\n').split()]
seq1 = set()
for i in seq:
    print(i, end = ' ')
    print('YES' if i in seq1 else 'NO')
    seq1.add(i)