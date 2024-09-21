def replace_negatives():
    #Введення списку чисел з клавіатури
    A = list(map(int, input('Enter a list of integers separated by spaces: ').split()))

    #Перевіряємо наявність від'ємних чисел
    has_negatives = any(num < 0 for num in A)
    if not has_negatives:
        print("No negative numbers found.")

    #Замінюємо всі від'ємні елементи на 0
    result = [0 if num < 0 else num for num in A]

    #Виводимо список
    print("Modified list:", result)

    return result

replace_negatives()

