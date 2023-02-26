#создаем список чисел
arr = input('Введите числа через пробел: ')
array_list = arr.split()
list_array = list(map(int, array_list))
print(list_array)



# сортировка по возрастанию
def Sortirovka_po_vozrastaniyu(list_array):
    for i in range( len(list_array)-1):
        for j in range(len(list_array) - 1):
            if (list_array[j] > list_array[j + 1]):
                list_array[j], list_array[j + 1] = list_array[j + 1], list_array[j]
    return list_array

print(Sortirovka_po_vozrastaniyu(list_array))

# алгоритм двоичного поиска
def binary_searrch(list_array, element, left, right):
    if left > right:
        return 'Таких чисел в списке нет'

    middle = (right + left) // 2
    if list_array[middle] == element:
        return middle
    elif element < list_array[middle]:
        return binary_searrch(list_array, element, left, middle-1)
    else:
        return binary_searrch(list_array, element, middle + 1, right)


element = int(input("Введите любое число : "))
if element not in list_array:
    print(f'Такого числа в списке {list_array} нет!')
    exit()
index_number = binary_searrch(list_array, element, 0, len(list_array))
print("Номер элемента в списке:", index_number, 'и равен: ', list_array[index_number])
if index_number == 0:
    print(f'Следующий номер в списке {index_number + 1} и равен {list_array[index_number+1]}')
elif index_number == int(len(list_array)-1):
    print(f'Предыдущий номер в списке {index_number - 1} и равен {list_array[index_number-1]}')
else:
    print(f'Предыдущий номер в списке {index_number - 1} и равен {list_array[index_number-1]}, cледующий номер в списке {index_number + 1} и равен {list_array[index_number+1]}')

