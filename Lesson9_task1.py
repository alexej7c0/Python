while True:                                                          
    n = int(input("Введите количество чисел "))                
    if 1 <= n <= 100000:                                               
        break
    else:
        print('Число должно быть в диапазоне: 1 <= N <= 100000 ')
        2 * 10e9

plenty = set()                  

while n > 0:                                                          
    num = int(input("Введите число "))                
    if 1 <= abs(num) <= 20000000000:
        plenty.add(num)
        n -= 1                                               
    else:    
        print('Число должно быть в диапазоне: 1 <= |N| <= 20000000000 ')

print(f"Количество разных чисел: {len(plenty)}")