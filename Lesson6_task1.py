n = int(input())
zeros = 0
for num in range(n):
    if int(input()) == 0:
        zeros += 1
print('Введено нулей:', zeros)
