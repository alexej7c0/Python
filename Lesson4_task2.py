num = int(input('Введите пятизначное целое число '))

units = num % 10
num //= 10

tens = num % 10
num //= 10

hundreds = num % 10
num //= 10

thousands = num % 10
num //= 10

tensOfThousands = num % 10
num //= 10

print(tens ** units * hundreds / (tensOfThousands - thousands))
