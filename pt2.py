print("Просто список с музычкой, гыгыгы")
print("Список поп-исполнителей/групп:"+"\n")
pop=['Michael Jackson', 'Beyonce', 'One Direction', 'Taylor Swift', 'Sam Smith', 
'One Republic', 'Rihanna', 'John Newman', 'Little Mix', 'Selena Gomez']
print(pop)
while True:
    b=input("Что вы хотите сделать со списком?"+"\n"+"1. Добавить элемент в конец списка"+"\n"
+"2. Добавить элемент в какой-либо из участков списка?"+"\n"+"3. Удаление элемента из списка"
+"\n"+"4. Вывод целиком списка"+"\n"+"5. Очищение самого списка"+"\n"+"6. Создание копиии списка"
+"\n"+"7. Майкл Джексон - король поп-музыки?"+"\n")
    if b=='1':
        print("Какой элемент вы хотите добавить?"+"\n")
        pop.append(input())
        print(pop)
    elif b=='2':
        poz=int(input("Выберите позицию на которой вы хотите расположить элемент: "))
        pop.insert(poz,input())
        print(pop)
    elif b=='3':
        poz=int(input("Выберите номер элемента, который хотите удалить: "))
        del pop[poz]
        print(pop)
    elif b=='4':
        print(pop)
    elif b=='5':
        del pop[:]
        print(pop)
    elif b=='6':
        pop_copy=pop[:]
        print("Созданная копия:"+"\n",pop_copy)
    elif b=='7':
        b=input()
        if b=='да' and 'Да':
            print("Ай, красава")
        elif b=='нет' and 'Нет':
            print("Даже я - компьютер и то, ничего не хочу иметь с тобой общего.")