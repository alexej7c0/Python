spec = input('К какому виду относится ваш питомец? ')
age = int(input('Сколько лет вашему питомцу? '))
name = input('Как зовут вашего питомца? ')

if age % 10 == 1:
    num = 'год'
elif 1 < (age % 10) < 5:
    num = 'года'
else:
    num = 'лет'
print(f'Это {spec} по кличке "{name}". Возраст: {age} {num}.')
