# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(zoo.index('lion') + 1, 'bear')
# print(zoo)
# zoo.remove('elephant')
# print(zoo)
# index_1 = zoo.index('lion') + 1
# index_2 = zoo.index('monkey') + 1
#
# print(index_1)
# print(index_2)

# emp_number = int(input('please enter a number of employees: '))
# salary_list = []
# for i in range(emp_number):
#     print(f'the salary of employer {i+1} is', end=' ')
#     salary = int(input())
#     salary_list.append(salary)
#
# for salary in salary_list:
#     if salary == 0:
#         salary_list.remove(salary)
#
# ramain_emp = len(salary_list)
# print('remain employees:', ramain_emp)
# print('the salaries:', salary_list)
# print(max(salary_list))
# print(min(salary_list))

def if_in_list(new_movie,list):
    for movie in list:
        if movie == new_movie:
            return True
    else:
        return False


#
# films = [
#
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#
#     'Мементо', 'Отступники', 'Деревня',
#
#     'Проклятый остров', 'Начало', 'Матрица'
#
# ]
#
# my_list = []
# while True:
#     print('your film list:', my_list)
#     my_movie = input('enter a movie: ', )
#     if if_in_list(my_movie, films):
#         print('the available commands: append, insert, remove')
#         command = input('input your command: ')
#     else:
#         print('there are no such film on the site')
#     if command == 'append':
#         if if_in_list(my_movie, my_list):
#             print('you already have this film in your list')
#         else:
#             my_list.append(my_movie)
#     if command == 'insert':
#         if if_in_list(my_movie, my_list):
#             print('you already have this film in your list')
#         else:
#             index = int(input('please enter an index: '))
#             my_list.insert(index + 1, my_movie)
#     if command == 'remove':
#         if if_in_list(my_movie, my_list):
#             my_list.remove(my_movie)
#         else:
#             print('there are no such film on the site')
#


# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
#
# first_company = [0, 0, 0]
#
# second_company = [1, 0, 0, 1, 1]
#
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
#
#
# print(main)
# print(main.count(0))

# the_first_sentence = 'Хм!!'
# the_second_sentence = '?!'
#
# if the_first_sentence.count('!') + the_first_sentence.count('?') > the_second_sentence.count('!') + the_second_sentence.count('?'):
#     print(f'{the_first_sentence} {the_second_sentence}')
# elif the_first_sentence.count('!') + the_first_sentence.count('?') < the_second_sentence.count('!') + the_second_sentence.count('?'):
#     print(f'{the_second_sentence} {the_first_sentence}')
# elif the_first_sentence.count('!') + the_first_sentence.count('?') == the_second_sentence.count('!') + the_second_sentence.count('?'):
#     print('ой')
#
# amt = int(input('pleaes enter an amount of pacs: '))
# list = []
# count = 0
# for i in range(amt):
#     list_pac = []
#     print(f'\npacs # {i + 1}')
#     for bit in range(4):
#         print(f'{bit + 1} bit:', end=' ')
#         bits = int(input(''))
#
#         list_pac.append(bits)
#     if list_pac.count(-1) <= 1:
#         list.extend(list_pac)
#     else:
#         print('there are a lot if mistakes')
#         count += 1

#
# print(list)
# print(count)
# print(list.count(-1))
#

#
# matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
#
# for i_list in matrix:
#     for i in i_list:
#         print(i, end=' ')
#     print()

# n = int(input('number: '))
# amt = int(input('number of people: '))
# while n % amt != 0:
#     print('mistake')
#     n = int(input('number: '))
#     amt = int(input('number of people: '))
# num = 1
# spisok = []
# for i in range(n // amt):
#     spisok.append(list(range(num, num + amt)))
#     num += amt
#
# print(spisok)

goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

new_fruit = input('input a new fruit: ')
new_price = int(input('input a new price: '))
new_good = []
new_good.append(new_fruit)
new_good.append(new_price)


print(goods)

for i in range(len(goods)):
    goods[i][1] += goods[i][1] * (8 / 100)

print(goods)


