from random import randint

col = int(input('Введите количество столбцов '))
row = int(input('Введите количество строк '))

matrix_1 = [[randint(-10, 10) for j in range(col)] for i in range(row)]
matrix_2 = [[randint(-10, 10) for j in range(col)] for i in range(row)]
matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(col)] for i in range(row)]

print()
print('matrix_1')
[print(i) for i in matrix_1]
print()

print('matrix_2')
[print(i) for i in matrix_2]
print()

print('matrix_3')
[print(i) for i in matrix_3]