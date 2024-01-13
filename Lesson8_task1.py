s = input('Введите слово ')
ans = 'no'
if s == s[::-1]:
    ans = 'yes'   
print(ans)