def sortlist():
    #Введення рядка з елементами
    A = input('Enter a list of numbers and letters separated by spaces: ').split()
    #Окремо для цифр і літер
    digits = []
    letters = []
    #Перебираємо елементи і розподіляємо їх між цифрами та літерами
    for elem in A:
        if elem.isdigit():  #Якщо елемент цифра
            digits.append(int(elem))
        elif elem.isalpha():  #Якщо елемент літера
            letters.append(elem)

    #Виведення результату
    print("Digits:", digits)
    print("Letters:", letters)

    return digits, letters
sortlist()

