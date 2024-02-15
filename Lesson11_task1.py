#  ОПРЕДЕЛЕНИЕ ФУНКЦИИ
def fct(num):
    count = 1
    for i in range(1, num + 1):
        count *= i
    
    list_fct = []
  
    for i in range(count, 0, -1):
        count1 = 1
        for j in range(1, i + 1):
            count1 *= j
        list_fct.append(count1)

    print(list_fct)


fct(int(input("Введите число: "))) # ВЫЗОВ ФУНКЦИИ