n1 = int(input("Сколько чисел будете вводить в первый список? "))
while n1 > 100000:
    print('Вводить можно не более 100000 чисел')
    n1 = int(input("Сколько чисел будете вводить? "))

list1 = []
for _ in range(n1):
    list1.append(int(input("Введите число: ")))

n2 = int(input("Сколько чисел будете вводить во второй список? "))
while n1 > 100000:
    print('Вводить можно не более 100000 чисел')
    n1 = int(input("Сколько чисел будете вводить? "))

list2 = []
for _ in range(n2):
    list2.append(int(input("Введите число: ")))

result = len(list1) + len(list2) - len(set(list1).union(list2))

print(f'Количество совпадающих чисел в списках: {result}')
