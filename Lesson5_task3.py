x = int(input('Введите минимальную сумму инвестиций... '))
a = int(input('Сколько денег у Майкла?... '))
b = int(input('Сколько денег у Ивана?... '))
ans = 0

if a >= x and b >= x:
    ans = 2
elif a >= x:
    ans = 'Mike'
elif b >= x:
    ans = 'Ivan'
elif a + b >= x:
    ans = 1

print(ans)
