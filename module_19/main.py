# dictionary = dict()
#
# number = int(input('please enter a number: '))
#
# for i_number in range(1, number + 1):
#     dictionary[i_number] = i_number ** 2
#
# print(dictionary)
#
# user_input = input('please enter a data: ').split(' ')
#
# university_dict = dict()
# university_dict['surname'] = user_input[0]
# university_dict['name'] = user_input[1]
# university_dict['city'] = user_input[2]
# university_dict['university'] = user_input[3]
# university_dict['grades'] = []
#
# for i_grade in user_input[4:]:
#     university_dict['grades'].append(int(i_grade))
#
# for i_number in university_dict:
#     print(i_number, '-', university_dict[i_number])
#

# phone_book = {'a': 3123,
#               'z': 3123,
#               'y': 3123,
#               'b': 3123}
# # name = ''
# while name != 'stop':
#     print('your phone_book:')
#     for i_number in phone_book:
#         print(i_number, '-', phone_book[i_number])
#     name = input('please input a name: ')
#     if name == 'stop':
#         break
#
#     elif name not in phone_book:
#         phone = int(input('please input a phone number: '))
#         phone_book[name] = phone
#
#     else:
#         print('the phone book already has consist the name')


# for i_number in sorted(phone_book):
# #     print(i_number, phone_book[i_number])
#
#
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# big_storage.update(small_storage)
#
# goods = input('please input a good: ')
#
# print(big_storage.get(goods))
#
# incomes = {
#
#     'apple': 5600.20,
#
#     'orange': 3500.45,
#
#     'banana': 5000.00,
#
#     'bergamot': 3700.56,
#
#     'durian': 5987.23,
#
#     'grapefruit': 300.40,
#
#     'peach': 10000.50,
#
#     'pear': 1020.00,
#
#     'persimmon': 310.00,
#
# }
# def keydef(dictionary, value):
#     for i_keys in dictionary:
#         if dictionary[i_keys] == value:
#             return i_keys
#
# print(sum(incomes.values()))
# print(min(incomes.values()))
# print(keydef(incomes, min(incomes.values())))
# incomes.pop(keydef(incomes, min(incomes.values())))
# print(incomes)

# text = 'Здесь что-то написано'
# text_dict = dict()
# for i_letter in text:
#     if i_letter in text_dict:
#         text_dict[i_letter] += 1
#     else:
#         text_dict[i_letter] = 1
#
# for i in sorted(text_dict):
#     print(i, '-', text_dict[i])
# print(max(text_dict.values()))
#
#
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
# for i_value in family_member['children']:
#     if i_value.get('name') == 'Bob':
#         print('yes')
#         surname = i_value.get('surname', 'nosurname')
#     print(i_value)
# print(surname)

# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# a_team = [
#     player['name']
#     for player in players_dict.values() if
#     player['team'] == 'A' and player['status'] == 'Rest'
# ]
#
# b_team = [
#     player['name']
#     for player in players_dict.values() if
#     player['team'] == 'B' and player['status'] == 'Training'
# ]
#
# c_team = [
#     player['name']
#     for player in players_dict.values() if
#     player['team'] == 'C' and player['status'] == 'Travel'
# ]
#
# print(a_team)
# print(b_team)
# print(c_team)
#
# punctuation = {'.', ',', ';', ':', '!', '?'}
# text = 'Я! Есть. Грут?! Я, Грут и Есть.'
# count = 0
# for i_letter in text:
#     if i_letter in punctuation:
#         count +=1
#
# print(count)
# import random
#
# nums_1 = [
#     29, 17, 10, 15, 13, 22, 12, 22, 7,
#     24, 26, 3, 11, 2, 3, 16, 19, 21, 2,
#     3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1
# ]
#
# nums_2 = [
#     16, 21, 30, 24, 5, 7, 23, 13, 11, 5,
#     21, 5, 19, 9, 12, 9, 15, 16, 29, 8,
#     16, 1, 22, 15, 16, 9, 1, 13, 21, 21
# ]
#
# first_set = set(nums_1)
# second_set = set(nums_2)
#
# print(first_set)
# print(second_set)
#
# print(min(first_set))
# print(min(second_set))
#
# first_set.remove(min(first_set))
# second_set.remove(min(second_set))
#
# first_set.add(random.randint(100, 200))
# second_set.add(random.randint(100, 200))
#
# print(first_set)
# print(second_set)
# print(first_set.union(second_set))
# print(first_set.intersection(second_set))
# print(second_set.difference(first_set))

# string = 'ab1n32kz2'
# num_set = set()
# for i in string:
#     if 'a' <= i <= 'z':
#         num_set.add(i)
#
#
# for num in num_set:
#     print(num, end='')
# import random
#
# first_tuple = tuple(random.randint(0, 5) for _ in range(10))
# second_tuple = tuple(random.randint(-5, 0) for _ in range(10))
# print(first_tuple)
# print(second_tuple)
# third_tuple = first_tuple + second_tuple
# fourth_tuple = first_tuple.__add__(second_tuple)
# print(third_tuple)
# print(fourth_tuple)
# print(third_tuple.count(0))
# import math
#
#
# def getting_square(radius, hight):
#     side = 2 * math.pi * radius * hight
#     full = side + 2 * math.pi * radius ** 2
#
#     return side, full
#
# side, full = getting_square(int(input('radius: ')), int(input('hight: ')))
#
# print(side)
# print(full)

#
# import random
#
#
# def change(nums):
#     index = random.randint(0, 5)
#     value = random.randint(100, 1000)
#     nums = list(nums)
#     nums[index] = value
#     nums = tuple(nums)
#     return nums, value
#
#
# my_nums = 1, 2, 3, 4, 5
#
# new_nums, rand_val = change(my_nums)
#
# print(new_nums, rand_val)
#
# new_nums, rand_val_2 = change(new_nums)
#
# rand_val_2 += rand_val
#
# print(new_nums, rand_val_2)

# string = 'so~mec~od~e'
#
# #for i, ii in enumerate([i for i in string]):
# for i, ii in enumerate(string):
#     if ii == '~':
#         print(i, end=' ')
# import random
#
# first = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)]
# second = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)]
# first_dict = {}
# second_dict = {}
#
# for index, letter in enumerate(first):
#     first_dict[index] = letter
#
#
# for index, letter in enumerate(second):
#     second_dict[index] = letter
#
# print(first)
# print(second)
# print(first_dict)
# print(second_dict)
#

# data = 'О Дивный Новый мир!'
# data1 = [100, 200, 300, 'буква', 0, 2, 'а']
# data2 = {18: 100, 24: 200, 54: 300, 12: 'буква', 4: 0, 5: 2, 6: 'а'}
#
#
# def isinstance(element, type):
#     # if type == tuple:
#     # element = [element[i] for i in element]
#
#     output = [letter for index, letter in enumerate(element) if index % 2 == 0]
#     return output
#
#
# print(isinstance(data, str))
# print(isinstance(data1, list))
# print(isinstance(data2, tuple))

#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for goods, price in incomes.items():
#     print('{goods} -- {price}'.format(
#         goods=goods,
#         price=price
# #     ))
#
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
# for i_keys, i_values in server_data.items():
#     print('{i_keys}:'.format(i_keys=i_keys))
#     for j_keys,j_values in i_values.items():
#         print('\t', '{0}: {1}'.format(j_keys, j_values))


# print([i_values for i_keys, i_values in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_keys % 2 == 0])
# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])

#
# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
#
# number = int(input('number of passport: '))
# series = int(input('series of passport: '))
#
# for i_keys in data:
#     if number in i_keys and series in i_keys:
#         print(data[i_keys][0], data[i_keys][1])
#
# phone_book = {
#     ('Андрей', 'Иванов'): 80808080,
#     ('Виталий', 'Петров'): 53432432,
#     ('Евгений', 'Жуков'): 79797,
#     ('Светлана', 'Хуева'): 534324324,
#
# }
#
# name = ''
#
# while name != 'stop':
#     flag = True
#     print('your phone_book:')
#     for person, phonenumber in phone_book.items():
#         print(person[0], person[1], phonenumber)
#     name = input('name: ')
#     surname = input('surname: ')
#     if name == 'stop':
#         break
#
#     for i_keys in phone_book:
#         if name in i_keys and surname in i_keys:
#             print('the phone book already has consist the name')
#             flag = False
#
#     if flag:
#         phone = int(input('please input a phone number: '))
#         phone_book[(name, surname)] = phone
#
# for person, phonenumber in phone_book.items():
#     print(person[0], person[1], phonenumber)

# def factorial(elem):
#     if elem == 1:
#         return 1
#
#     result = elem * factorial(elem - 1)
#     return result
#
# print(factorial(13))

# def power(a, n):
#     if n == 1:
#         return a
#
#     y = power(a, n - 1)
#     result = a * y
#
#     return result
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))
#


# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# def get_value(user_dict, key):
#     if user_dict.get(key):
#         return user_dict.get(key)
#
#     for sub_key in user_dict.values():
#         if isinstance(sub_key, dict):
#             result = get_value(sub_key, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# print(get_value(site, 'div'))

#
# import random
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list[:], 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
# change_dict(common_dict)
#
# print(common_dict)
# print(nums_list)
# print(some_dict)
# print(uniq_nums)
#
# user_input = input()
# print(id(user_input))
# print(type(user_input))
