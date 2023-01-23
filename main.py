# Программа находит четные числа в списке.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

# Программа преобразовывает список строк в список чисел.

b = list(map(int, ['1', '2', '3', '6', '8']))

print(b)

# Программа выводит список городов заглавными буквами.

cities = ['Москва', 'Уфа', 'Смоленск', 'Тверь']
b = list(map(str.upper, cities))
print(b)

# Программа проверяет совпадения в двух списках.

list1 = ['Python', 'CSharp', 'Java', 'Go']
list2 = ['Python', 'Scala', 'JavaScript', 'Go', 'PHP', 'CSharp']

def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True

ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))

print('Отфильтрованный список:', out_filter)

# Создание нового списка участников с кортежами из индекса и имен участников.

participants = ['John', 'Tom', 'Jack']
data = list(enumerate(participants))
print(data)

# Объединение имен и номеров сотрудников.

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

print(zipped_list)