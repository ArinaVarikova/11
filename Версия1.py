from ast import*
print("Запись на техническое обслуживание транспортных средств\n")
list1 = []
with open('l', 'r') as f:
    for line in f:
        items = literal_eval(line)
        for i in items:
            list1.append(i)
    
it = True
while it:
    a = (input(f"Выберите номер команды, которую хотите выполнить:\n"
                "1.Фильтр всех существующих записей\n"
                "2.Добавить запись\n"
                "3.Изменить запсь\n"
                "4.Удалить запись\n"
                "5.Поиск данных в записи \n"
                "6.Завершить работу с файлом\n"
                "Номер команды:"))
    if a == '1':
        for x in list1:
            print(x)
    elif a == '2':
        wri = []
        lt = True
        while lt:
            try:
                l = int(input("Введите номер заказа\n"))
                n = 'Заказ' + ' ' + str(l)
                wri = wri + [n]
                lt = False
            except:
                print('Введено недопустимое значение.\n')
                
        c = input('Введите фамилию владельца. Пример верного ввода: Иванов\n')
        wri = wri + [c]
        q = input('Введите имя владельца. Пример верного ввода: Иван\n')
        wri = wri + [q]
        b = input("Введите адрес владельца, номер дома и улица, через пробелы. Пример верного ввода: Ленина 32\n")
        wri = wri + [b]
        d = input("Введите электронную почту владельца. Пример верного ввода:Ivan@mail.ru\n")
        wri = wri + [d]
        
        rt = True
        while rt:
            z = input("Введите категорию транспортного средства. Допустимые значения для ввода: мотоцикл, легковой, грузовой ,мопед, авобус\n")
            if z == 'мотоцикл' or z == 'легковой' or z == 'грузовой' or z == 'мопед' or z == 'автобус':
                wri =  wri + [z]
                rt = False
            else:
                print('Введено недопустимое значение.\n')
        
        ot = True
        while ot:
            p = input("Введите состояние фар. Допустимые значения для ввода: включены, выключены\n")
            if p == 'включены' or p == 'выключены':
                wri = wri + [p]
                ot = False
            else:
                print('Введено недопустимое значение.\n')
                
        qt = True
        while qt:
            t = input("Введите состояние дверей. Допустимые значения для ввода: закрыты, открыты\n")
            if t == 'закрыты' or t == 'открыты':
                wri = wri + [t]
                qt = False
            else:
                print('Введено недопустимое значение.\n')
                
       
        kt = True
        while kt:
            k = input("Введите с маленькой буквы месяц в котром хотите записаться\n")
            
            if k == 'май' or k == 'январь' or k == 'февраль' or k == 'март' or k == 'апрель' or k == 'июнь'  or k == 'июль' or k == 'август' or k == 'сентябрь' or k == 'октябрь' or k == 'ноябрь' or k == 'декабрь':
                wri = wri + [k] 
                kt = False
            else:
                print('Введено недопустимое значение.\n')
                
        gt = True
        while gt:
            g = input("Введите номер дня. Помните, что 31 число - санитарный день, запись на него недоступна\n")
            if g == '1' or g == '2' or g == '3' or g == '4' or g == '5' or g == '6' or g == '7' or g == '8' or g == '9' or g == '10' or g == '11' or g == '12' or g == '13' or g == '14' or g == '15' or g == '16' or g == '17' or g == '18' or g == '19' or g == '20' or g == '21' or g == '22' or g == '23' or g == '24' or g == '25' or g == '26' or g == '27' or g == '28' or g == '29' or g == '30':
                wri = wri + [g] 
                gt = False
            else:
                print('Введено недопустимое значение.\n')
        pt = True
        while pt:
            m = input("Введите время записи, Допустимые значения для ввода: 8:00, 10:00, 12:00, 14:00, 16:00, 18:00\n")
            if m == '8:00' or m == '10:00' or m == '12:00' or m == '14:00' or m == '16:00' or m == '18:00':
                wri = wri + [m]
                pt = False
            else:
                print('Введено недопустимое значение.\n')
        d = wri[0]
        f = wri[8]
        g = wri[9]
        h = wri[10]
        for x in list1:
            if ((f  in x) and (g in x) and (h in x)):
                print("Дата уже занята.\n")
                break
            if (d in x):
                 print("Заказ с таким нмером уже существует.\n")
                 break
        else:    
            list1 = list1 + [wri]  
            print("Запись создана.\n")
            
               
    elif a == '3':
        po = input('Введите номер заказа, который хотите изменить. Пример верного ввода: Заказ 6.\n')
        for x in list1:
            if po in x:
                while po in x:
                    print(x)
                    break
                break
        else:
            print('Нет такого номера заказа\n')
            continue
        j = input("Вы уверены, что именно этот заказ хотите изменить?\n")
        if j == 'да':
            ip = input('Введите, что изменить\n')
            for x in list1:
                if (ip in x) and (po in x):
                    m = input('Введите новое состояние\n')
                    d = []
                    for x in list1:
                        c = [(m if i == ip else i) for i in x]
                        d = d + [c]
                        list1 = d
                    print("Запись изменена.\n")
                    break
            else:
                print("Таких данных нет.\n")
                continue
        elif j == 'нет':
            print("Выполнение команды прекращено.\n")
        else:
            print('Введено недопустимое значение.\n')
    elif a == '4':
        po = input('Введите номер заказа, который хотите удалит. Пример верного ввода: Заказ 6.\n')   
        for x in list1:
            if po in x:
                while po in x:
                    print(x)
                    break
                break
        else:
            print('Нет такого номера заказа\n')
            continue
        j = input("Вы уверены, что именно этот заказ хотите удаить?\n")
        if j == 'да':
            c = []
            for x in list1:
                if po not in x:
                    c = c + [x]
                    list1 = c   
            print("Запись удалена\n")
        elif j == 'нет':
            print("Выполнение команды прекращено.\n")
        else:
            print('Введено недопустимое значение.\n')
    elif a == '5':
        po = input('Введите критерий поиска\n')
        for x in list1:
            if po in x:
                while po in x:
                    print(x)
                    break
    elif a == '6':
        it = False
    else:
        print("Нет такой команды.\n")
with open('l', 'w') as f:
            f.write(str(list1))
