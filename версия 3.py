from ast import*
import tabulate


print("Запись на техническое обслуживание транспортных средств\n")
def poisk(po):
    for x in list1:
        if po in x:
            while po in x:
                print(x)
                break

        
def read():
    
    result = tabulate.tabulate(list1)
    print(result)

def ty():
    yt = True
    m = []
   
    while yt:
        po = input('Введите нужный номер заказа. Пример верного ввода: Заказ 1\n')
        m = m+[po]
        k = []
        for x in list1:
            if po in x:
                l = 1
                k = k+[str(l)]
        else:
            l = 0
            k = k+[str(l)]
        if k[0] == '1':
            for x in list1:
                if po in x:
                    while po in x:
                        print(x)
                        break
                    break
            yt = False
        elif k[0]=='0':
            print('Нет такого номера заказа\n')
    po = m[0]
    return po
def wr():
    with open('l', 'w') as f:
        f.write(str(list1)) 
class Order:
    def __init__(self, order_number, month, date, time, customer, car):
        self.order_number = order_number
        self.month = month
        self.date = date
        self.time = time
        self.customer = customer
        self.car = car
        self.customer.hystory_order_numbers.append(order_number)
        self.customer.hystory_order_time.append(time)
        self.customer.hystory_order_date.append(date)
        self.customer.hystory_order_customer.append(customer)
        self.customer.hystory_order_car.append(car)

class Customer:
    def __init__(self, vorname, name, address, contact):
        self.vorname = vorname
        self.name = name
        self.address = address
        self.contact = contact
        self.hystory_order_numbers = []
        self.hystory_order_time = []
        self.hystory_order_date = []
        self.hystory_order_customer = []
        self.hystory_order_car = []


class Car:
    def __init__(self, type, lights, doors):
        self.type = type
        self.lights = lights
        self.doors = doors
        
list1 = []

with open('l', 'r') as f:
    for line in f:
        items = literal_eval(line)
        for i in items:
            a = i
            list1.append(i)
it = True
while it:
    a = (input(f"Выберите номер команды, которую хотите выполнить:\n"
              "1.Вывод всех существующих записей\n"
              "2.Добавить запись\n"
              "3.Изменить запсь\n"
              "4.Удалить запись\n"
              "5.Поиск по существующим элементам\n"
              "6.Завершить работу с файлом\n"
              "Номер команды:"))
    if a == '1':
       read()
    elif a == '2':
        wri = []
        lt = True
        while lt:
            try:
                l = int(input("Введите номер заказа\n"))
                n = 'Заказ' + ' ' + str(l)
                wri.append(n)
                lt = False
            except:
                print('Введено недопустимое значение.\n')
                
        c = input('Введите фамилию владельца. Пример верного ввода: Иван\n')
        wri.append(c)
        q = input('Введите имя владельца. Пример верного ввода: Иван\n')
        wri.append(q)
        b = input("Введите адрес владельца, номер дома и улица, через пробелы. Пример верного ввода: Ленина 32\n")
        wri.append(b)
        d = input("Введите электронную почту владельца. Пример верного ввода:Ivan@mail.ru\n")
        wri.append(d)
        
        rt = True
        while rt:
            z = input("Введите категорию транспортного средства. Допустимые значения для ввода: мотоцикл, легковой, грузовой ,мопед, авобус\n")
            if z == 'мотоцикл' or z == 'легковой' or z == 'грузовой' or z == 'мопед' or z == 'автобус':
                wri.append(z)
                rt = False
            else:
                print('Введено недопустимое значение.\n')
        
        ot = True
        while ot:
            p = input("Введите состояние фар. Допустимые значения для ввода: включены, выключены\n")
            if p == 'включены' or p == 'выключены':
                wri.append(p)
                ot = False
            else:
                print('Введено недопустимое значение.\n')
                
        qt = True
        while qt:
            t = input("Введите состояние дверей. Допустимые значения для ввода: закрыты, открыты\n")
            if t == 'закрыты' or t == 'открыты':
                wri.append(t)
                qt = False
            else:
                print('Введено недопустимое значение.\n')
                
       
        kt = True
        while kt:
            k = input("Введите с маленькой буквы месяц в котром хотите записаться\n")
            
            if k == 'май' or k == 'январь' or k == 'февраль' or k == 'март' or k == 'апрель' or k == 'июнь'  or k == 'июль' or k == 'август' or k == 'сентябрь' or k == 'октябрь' or k == 'ноябрь' or k == 'декабрь':
                wri.append(k)
                kt = False
            else:
                print('Введено недопустимое значение.\n')
              
        gt = True
        while gt:
            g = input("Введите номер дня. Помните, что 31 число - санитарный день, запись на него недоступна\n")
            if g == '1' or g == '2' or g == '3' or g == '4' or g == '5' or g == '6' or g == '7' or g == '8' or g == '9' or g == '10' or g == '11' or g == '12' or g == '13' or g == '14' or g == '15' or g == '16' or g == '17' or g == '18' or g == '19' or g == '20' or g == '21' or g == '22' or g == '23' or g == '24' or g == '25' or g == '26' or g == '27' or g == '28' or g == '29' or g == '30':
                wri.append(g)
                gt = False
            else:
                print('Введено недопустимое значение.\n')
        pt = True
        while pt:
            m = input("Введите время записи, Допустимые значения для ввода: 8:00, 10:00, 12:00, 14:00, 16:00, 18:00\n")
            if m == '8:00' or m == '10:00' or m == '12:00' or m == '14:00' or m == '16:00' or m == '18:00':
                wri.append(m)
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
            customer = Customer(wri[1],wri[2],wri[3], wri[4])
            car = Car(wri[5],wri[6],wri[7])
            order = Order(wri[0], wri[8],wri[9],wri[10], customer, car)
            write1 = [order.order_number,customer.vorname, customer.name, customer.address, customer.contact,car.type, car.lights, car.doors, order.month, order.date, order.time]
            list1.append(write1)
            print("Запись создана")
                  

    elif a == '3':
        read()
        po = (ty())
        j = input("Вы уверены, что именно этот заказ хотите изменить?\n")
        if j == 'да':
            ip = input('Введите, что изменить\n')
            for x in list1:
                if (ip in x) and (str(po) in x):
                    m = input('Введите новое состояние\n')
                    c = x
                    c[c.index(ip)] = m
                    list1.append(c)
                    list1.remove(x)
                    print('Запись изменена')
                    break
            else:
                print("Таких данных нет.\n")
                continue
        elif j == 'нет':
            print("Выполнение команды прекращено.\n")
        else:
            print('Введено недопустимое значение.\n')
        wr()
    elif a == '4':
       read()
       po = (ty())
       j = input("Вы уверены, что именно этот заказ хотите удаить?\n")
       if j == 'да':
            c = []
            for x in list1:
                if po in x:
                    list1.remove(x) 
            print("Запись удалена\n")
       elif j == 'нет':
           print("Выполнение команды прекращено.\n")
       else:
           print('Введено недопустимое значение.\n')
       wr() 
    
    elif a == '5':
        read()
        po = input('Введите критерий поиска\n')
        poisk(po)
                                     
    elif a == '6':
        it = False
    else:
        print("Нет такого номера команды\n")
wr()
