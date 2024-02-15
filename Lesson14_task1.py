my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def rec(n = 0):
    print(my_list[n])
    n += 1
    
    if n == len(my_list):
        print('Конец списка')
        return
    rec(n)
    
rec()