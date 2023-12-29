while True:
    x = int(input("Введите число 'X': "))
    if x > 2e9:
        print("Число 'X' не должно превышать 2000000000 ")
    else:
        break
count = 0

for i in range(1, x + 1):
    if x % i == 0:
        count += 1
print(f"Количество делителей числа {x} равно: {count}")
