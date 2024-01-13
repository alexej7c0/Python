while True:                                                          #
    m = int(input("Введите грузоподъёмность лодки "))                # Ввод грузоподъёмности с проверкой условия
    if 1 <= m <= 10e6:                                               #
        break
    else:
        print('Число должно быть в диапазоне: 1 <= m <= 10000000 ')

while True:                                                          #
    n = int(input("Введите количество рыбаков "))                    # Ввод кол-ва рыбаков с проверкой условия
    if 1 <= n <= 100:                                                #
        break
    else:
        print('Число должно быть в диапазоне: 1 <= n <= 100 ')

fishermen = []                                                       # список масс рыбаков

while n > 0:                                                         #
    ai = int(input('Введите массу рыбака '))                         # Ввод рыбаков с проверкой условия
    if 1 <= ai <= m:                                                 #
        fishermen.append(ai)
        n -= 1
    else:
        print('Число должно быть в диапазоне: 1 <= ai <= m ')

boat_counter = 0                                                     # количество лодок

while len(fishermen) > 0:                                            
    in_boat = []                                                     # список людей в лодке
    boat_load = m                                                    # количество оставшегося места в лодке
                                                      
    for i in fishermen:

        if i <= boat_load:
            boat_load -= i
            in_boat.append(i)

    boat_counter += 1
    
    for i in in_boat:
        fishermen.remove(i)
print(boat_counter)