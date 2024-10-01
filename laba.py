# Ініціалізація словника з даними про багаж пасажирів (словник зі списками як значеннями)
baggage = {
    1: [3, 30],  # [items, weight]
    2: [1, 20],
    3: [4, 50],
    4: [2, 15],   
    5: [1, 10],
    6: [5, 60],
    7: [2, 35],
    8: [3, 25],
    9: [1, 24],
    10: [2, 28],
}

# Функція для виведення всіх записів словника
def print_baggage(baggage):
    for bag_id, values in baggage.items():
        items, weight = values
        print(f"Bag № {bag_id}: Items = {items}, Weight = {weight} кг")
        
# Функція для додавання нового запису
def add_baggage(baggage, bag_id, items, weight):
    if bag_id in baggage:
        print("Такий багаж вже існує.")
    else:    
        baggage[bag_id] = [items, weight]  # Додаємо новий запис у вигляді списку
        print(f"Added Bag № {bag_id}: Items = {items}, Weight = {weight}")

# Функція для видалення запису
def remove(baggage, bag_id):
    if bag_id in baggage:
        del baggage[bag_id]  # Видаляємо запис за ключем
        print(f"Removed Bag {bag_id}")
    else:
        print(f"Bag {bag_id} not found!")

# Функція для перегляду словника за відсортованими ключами
def view_sorted_baggage(data):
    for bag_id in sorted(data.keys()):
        print(f"Багаж {bag_id}: Items = {data[bag_id][0]}, Weight = {data[bag_id][1]}")

# Завдання а: Кількість пасажирів, які мають більше двох речей
def passengers1(data):
    count = sum(1 for items, weight in data.values() if items > 2)
    print(f"Кількість пасажирів, які мають більше двох речей: {count}")

# Завдання б: Чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25кг
def passenger2(data):
    found = any(items == 1 and weight < 25 for items, weight in data.values())
    if found:
        print("Є пасажир з однією річчю вагою менше 25 кг.")
    else:
        print("Немає пасажира з однією річчю вагою менше 25 кг.")

# Завдання в: Номер багажу, в якому вага однієї речі відрізняється від загальної середньої не більше ніж на 0.5 кг
def baggage3(data):
    total_items = sum(items for items, weight in data.values())
    total_weight = sum(weight for items, weight in data.values())
    avg_weight_per_item = total_weight / total_items if total_items > 0 else 0

    for bag_id, (items, weight) in data.items():
        if items > 0 and abs((weight / items) - avg_weight_per_item) <= 0.5:
            print(f"Багаж {bag_id} має вага речей, яка відповідає умові.")
            return
    print("Немає багажу, який відповідає умові.")

# Організований діалог з користувачем
def dialog():
    while True:
        print("\nОберіть дію:")
        print("1: Вивести всі дані про багаж")
        print("2: Додати новий запис про багаж")
        print("3: Видалити запис про багаж")
        print("4: Переглянути багаж за відсортованими ключами")
        print("5: Виконати завдання а")
        print("6: Виконати завдання б")
        print("7: Виконати завдання в")
        print("0: Вийти")

        choice = input("Введіть номер дії: ")

        if choice == '1':
            print_baggage(baggage)

        elif choice == '2':
            try:
                bag_id = int(input("Введіть номер багажу: "))
                items = int(input("Кількість речей: "))
                weight = float(input("Загальна вага: "))
                add_baggage(baggage, bag_id, items, weight)
            except ValueError:
                print("Помилка: Некоректні дані.")

        elif choice == '3':
            try:
                bag_id = int(input("Введіть номер багажу для видалення: "))
                remove(baggage, bag_id)
            except ValueError:
                print("Некоректний номер")

        elif choice == '4':
            view_sorted_baggage(baggage)

        elif choice == '5':
            passengers1(baggage)

        elif choice == '6':
            passenger2(baggage)

        elif choice == '7':
            baggage3(baggage)

        elif choice == '0':
            print("Вихід.")
            break

        else:
            print("Невірний вибір.")

dialog()


