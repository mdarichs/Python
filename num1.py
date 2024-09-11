#Введення кількості елементів у масиві
N = int(input("N = "))

#Введення елементів масиву
print(f"Enter {N} array elements:")
arr = [float(input()) for _ in range(N)]
#Виведення заданого масиву
print("Original array: ", arr)

# Ініціалізація змінної для мінімального від'ємного елемента
min = None

#Знаходження мінімального елемента масиву
for num in arr:
  if num < 0: #перевірка на від'ємність
      if min is None or num < min: #перевірка для збереження мінімуму
          min = num

#Виведення результату
if min is not None:
  print("Minimum negative element: ", min)
else:
  print("No negative elements in the array.")
