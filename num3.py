def search():
    #Введення тексту
    A = input("Enter a text: ")

    #Перетворення на нижній регістр
    B = A.lower()

    #Множина голосних літер
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    #Підрахунок голосних
    vowel_count = sum(1 for char in B if char in vowels)

    #Виведення результату
    print("Text:", B)
    print("Number of vowels:", vowel_count)

    return vowel_count

search()
