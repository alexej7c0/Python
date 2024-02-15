########   ФУНКФУНКЦИЯ ДОБАВЛЕНИЯ НОВОГО ПИТОМЦА   ########

def create():
    id = id_count

    pets[id] = {}

    pets[id]['Имя'] = input("Введите имя питомца: ")
    pets[id]['Вид питомца'] = input("Введите вид питомца: ")
    pets[id]['Возраст питомца'] = only_num("Введите возраст питомца: ", 'Возраст должен быть целым числом ')
    pets[id]['Имя владельца'] = input("Введите имя владельца: ")

    print(f'ID вашего питомца: {id}\n')
    return id_count + 1


#######   ФУНКФУНКЦИЯ ВЫВОДА ИНФОРМАЦИИ О ПИТОМЦЕ   #######
 
def read():
    id = only_num('Введите ID питомца: ', 'ID должен быть целым числом ')
    if id not in pets:
      return False
    if pets[id]['Возраст питомца'] % 10 == 1 and pets[id]['Возраст питомца'] % 100 not in [11, 12, 13]:
        word = "год"
    elif pets[id]['Возраст питомца'] % 10 in (2, 3, 4) and pets[id]['Возраст питомца'] % 100 not in [11, 12, 13]:
        word = "года"
    else:
        word = "лет"
    print(f'Это {pets[id]["Вид питомца"]} по кличке "{pets[id]["Имя"]}". Возраст питомца: {pets[id]["Возраст питомца"]} {word}. Имя владельца: {pets[id]["Имя владельца"]}\n')


######   ФУНКЦИЯ ОБНОВЛЕНИЯ ИНФОРМАЦИИ О ПИТОМЦЕ   ########

def update():
    id = only_num('Введите ID питомца: ', 'ID должен быть целым числом ')
    if id not in pets:
      return False

    print(f"Имя питомца, текущее значение: {pets[id]['Имя']}")
    pets[id]['Имя'] = input("Введите новое значение имени: ")
  
    print(f"Вид питомца, текущее значение: {pets[id]['Вид питомца']}")
    pets[id]['Вид питомца'] = input("Введите новое значение вида: ")
  
    print(f"Возраст питомца, текущее значение: {pets[id]['Возраст питомца']}")
    pets[id]['Возраст питомца'] = only_num("Введите новое значение возраста: ", 'Возраст должен быть целым числом ')
  
    print(f"Имя владельца, текущее значение: {pets[id]['Имя владельца']}")
    pets[id]['Имя владельца'] = input("Введите новое значение имени владельца: ")


##############   ФУНКЦИЯ УДАЛЕНИЯ ПИТОМЦА   ###############

def delete():
    id = only_num('Введите ID питомца: ', 'ID должен быть целым числом ')
    if id not in pets:
      return False
    del pets[id]
    print(f'Питомец с ID {id} удален\n')

########   ФУНКЦИЯ ПРОВЕРКИ ДЛЯ ЧИСЛОВОГО ВВОДА   #########

def only_num(input_mess, correct_mess): 
    while True:
        user_input = input(input_mess)
        if user_input.isdigit():
            return int(user_input)    
        else:
          print(correct_mess)


###########   ФУНКЦИЯ ВЫВОДА СПИСКА ПИТОМЦЕВ   ############

def pets_list():
    for key in pets:
        print(f'ID: {key}, Вид: {pets[key]["Вид питомца"]}, Кличка: {pets[key]["Имя"]}, Возраст: {pets[key]["Возраст питомца"]}, Владелец: {pets[key]["Имя владельца"]}\n')     


id_count = 1               
pets = {}                


####################      КОМАНДЫ     #####################

print('КОМАНДЫ:')
print('Добавить питомца - "create"')
print('Информация о питомце - "read"')
print('Обновить информацию о питомце - "update"')
print('Удалить питомца - "delete"')
print('Вывести список питомцев - "list"\n')


####################   ГЛАВНЫЙ ЦИКЛ   #####################

command = 'wait...'
while command != 'stop':
    match command:
        case 'wait...':
            command = input('Введите команду ')
        case 'create':
            id_count = create()
            command = 'wait...'
        case 'read':
            read() 
            command = 'wait...'
        case 'update':
            update()
            command = 'wait...'
        case 'delete':
            delete()
            command = 'wait...'
        case 'list':
            pets_list()
            command = 'wait...'
        case _:
            print('Ошибка ввода, введите корректную команду\n')
            command = 'wait...'