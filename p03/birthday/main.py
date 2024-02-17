print("\nПривіт")
print("Хочеш я вгадаю коли в тебе день народження?")
choise = input('Бажаєте продовжити y/n: ')

if choise == "y":
    print()
    age = int(input('Ваш вік: '))
    
    print("1. Помнож на 2 число дня свого народження")
    print("2. Тепер додай 5")
    print("3. Помнож на 50")
    print("4. Додай номер місяця свого народження")
    print("Яке число ти отримав?")

    number = int(input('Число = '))
    number -= 250
    date = number // 100
    month = number - 100*date

    if month == 1:
        month = "січня"
        print("Твій день народження %s %s" %(date, month))
    elif month == 2:
        month = "лютого"
        print("Твій день народження %s %s" % (date, month))
    elif month == 3:
        month = "березня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 4:
        month = "квітня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 5:
        month = "травня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 6:
        month = "червня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 7:
        month = "липня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 8:
        month = "серпня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 9:
        month = "вересня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 10:
        month = "жовтня"
        print("Твій день народження %s %s" % (date, month))
    elif month == 11:
        month = "лютого"
        print("Твій день народження %s %s" % (date, month))
    elif month == 12:
        month = "грудня"
        print("Твій день народження %s %s" % (date, month))
    else:
            print("Щось пішло не так!")

else:
    print("Зустрінемось пізніше!")