while True:
    s = input('Введите слово ')
    if len(s) <= 1000:
        break
    else:
        print('Слово должно быть короче 1000 символов ')    
s1 = s[0]
for c in range(1, len(s)):
    if s[c] == ' ' == s[c - 1]:
        continue
    else:
        s1 += s[c]
print(s1)