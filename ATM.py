print("Добро пожаловать!")

money = []
sumMoney = 0
currencySum = 0
moneyCurrency = []

takeMoney = input("Желаете продолжить? Да или нет: ")

while True:
    if takeMoney == "Да":
        operation = int(input("Добавить средства(1) или снять(2)? 1 или 2, 0 - выход? "))
        if operation == 1:
            addMoney = int(input("Сколько вы желаете добавить? 5, 10 или 20 рубелей? "))
            if addMoney == 5 or addMoney == 10 or addMoney == 20:
                print("Вы добавили " + str(addMoney) + " рублей")
                appMoney = money.append(addMoney)
                sumMoney = (sum(money))
                print("У вас на счету " + str(sumMoney) + " рублей")
            else:
                print("Ошибка! Нет такой купюры")

        elif operation == 2:
            takeBills = int(input("Сколько вы желаете снять? "))
            if takeBills == 5 or takeBills == 10 or takeBills == 20:
                if takeBills > sumMoney:
                    print("Недостаточно средств")
                else:
                    currency = moneyCurrency.append(takeBills)
                    currencySum = (sum(moneyCurrency))
                    endSum = sumMoney - currencySum
                    if endSum < 0:
                        print("Ошибка!")
                    else:
                        print("У вас на счету " + str(endSum) + " рублей")
            else:
                print("Нет такой купюры")
        elif operation == 0:
            break
    else:
        print("До свидания! Всего доброго!")
        break
else:
    None



