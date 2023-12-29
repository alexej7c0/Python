word = input('Введите слово маленькими английскими буквами ')
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
tot_cons, tot_vow = 0, 0

for key in word:
    if key in 'aeiou':
        tot_vow += 1

        if key in vowels:
            vowels[key] += 1

print('Количество согласных:', len(word) - sum(vowels.values()))
print('Количество гласных:', sum(vowels.values()))
for key in vowels:
    if vowels[key] > 0:
        print(f'Количество букв "{key}" :', vowels[key])
    else:
        print(vowels[key] > 0)
