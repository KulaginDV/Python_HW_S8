import os, re

# форматирование телефонного номера
def phone_format(n):
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]

# Функция вывода телефонной книги в консоль
def printData(data):
    phoneBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Фамилия        Имя          Номера телефонов")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "Фамилия": lastName,
                "Имя": name,
                "Телефон": phone_format(phone),
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

    print(splitLine)

# Функция открытия телефонной книги
def showContacts(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- нажмите любую клавишу ---")

# Функция добавления нового контакта в телефонную книгу
def addContact(fileName):  
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию контакта: ") + ","
        res += input("Введите имя контакта: ") + ","
        res += input("Введите телефон контакта: ")

        file.write(res + "\n")

    input("\nКонтакт успешно добавлен!\n--- нажмите любую клавишу ---")

 # Функция поиска контактов в телефонной книге
def findContact(fileName): 
    os.system("cls")
    target = input("Введите элемент контакта для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"Нет контакта с таким элементом '{target}'.")

    input("--- нажмите любую клавишу ---")

# Функция изменения информации в контакте
def changeContact(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для изменения или нажмите 0 для возврата: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый телефон: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен!")
                input("\n--- нажмите любую клавишу ---")
        else:
            return

# Функция удаления контакта из телефонной книги
def deleteContact(fileName):  
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для удаления или нажмите 0 для возврата в главное меню: ")
        )
        if numberContact != 0:
            print(f"Удаление записи: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- нажмите любую клавишу ---")

# Функция рисования интерфейса главного меню
def drawInterface():  
    print("#####   Телефонный справочник   #####")
    print("=" * 26)
    print(" [1] -- Показать контакты")
    print(" [2] -- Добавление контактов")
    print(" [3] -- Поиск контактов")
    print(" [4] -- Изменение контактов")
    print(" [5] -- Удаление контактов")
    print("\n [0] -- Выход")
    print("=" * 26)

# Функция реализации главного меню
def main(file_name):  
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите число от 1 до 5 или нажмите 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Спасибо!")
            return


path = "Телефонный справочник.txt"

main(path)