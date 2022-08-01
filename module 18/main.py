# name = input('name: ')
# debt = int(input('debt: '))
#
# # print('{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!'.format(name, debt))
# ip_list = []
# for i in range(4):
#     while True:
#         number = int(input('please input {0} number: '.format(i+1)))
#         if 0 <= number <= 255:
#             ip_list.append(number)
#             break
#         else:
#             print('the mistake, try again')
#
#
# for i_num in ip_list:
#     print('{0}.'.format(i_num), end='')
#
# ip_adress = ('\n{0}.{1}.{2}.{3}'.format(
#     ip_list[0],
#     ip_list[1],
#     ip_list[2],
#     ip_list[3]
# ))
# # print(ip_adress)
# word_list = [input('input the world: ') for i in range(3)]
# text_list = input('input the text: ').split()
#
# for word in word_list:
#     count = 0
#     for text in text_list:
#         if word == text:
#             count += 1
#     print('\n{word} - {count}'.format(
#         word=word,
#         count=count
#     ))
#
# text_list = input('input the text: ').split()
# print(' '.join(text_list))

# template = input('please input an template: ')
#
# names_list = input('please input a name: ').split(', ')
# ages_list = input('please input an age: ').split()
#
# for i in range(len(names_list)):
#     print(template.format(
#         name=names_list[i],
#         age=ages_list[i]
#     ))

# def encryption(letter):
#     alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     if letter in alph:
#         letter = alph[(alph.index(letter) + 3) % len(alph)]
#     return letter
#
# text = input('введите сообщение: ').lower()
# answer = ''.join([encryption(letter) for letter in text])
#
#
#
# # print(answer)
# path = input('please entet a path: ')
# disk = input('please enter a tittle of disk: ')
# extension = input('please enter an extension: ')
#
# if not path.startswith(disk.lower()):
#     print('mistake')
# elif not path.endswith(extension.lower()):
#     print('mistake')
# else:
#     print(path)

text = input('please input a text: ')



lower_list = [letter for letter in text if letter.islower()]
upper_list = [letter for letter in text if letter.isupper()]
if len(lower_list) > len(upper_list):
    print(text.lower())
else:
    print(text.upper())
