n = int(input('Введите целое число '))
sign, even_or_odd = '', ''

if n > 0:
    sign = "положительное"
elif n < 0:
    sign = "отрицательное"
else:
    sign = "нулевое"

if sign != "нулевое":
    if n % 2 == 0:
        even_or_odd = "четное"
    else:
        even_or_odd = "нечетное"
    print(f"{sign} {even_or_odd} число")
else:
    print(sign, "число")
