n = [int(input("Введите число ")) for _ in range(int(input('Введите число "N"')))]
n.insert(0, n.pop(-1))
print(n)