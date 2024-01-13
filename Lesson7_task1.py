n = int(input('Введите число '))
lst = []
for _ in range(n):
    lst.append(int(input('Введите число ')))
print(list(reversed(lst)))
