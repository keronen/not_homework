first_number = float(input('введите первое число: '))
second_number = float(input('введите второе число: '))

def revers(number):
    rev_number1 = ''
    rev_number2 = ''
    flag = False
    for i in reversed(str(number)):
        if i != '.' and flag == False:
            rev_number2 += i
        elif i == '.':
            flag = True
        else:
            rev_number1 += i
    rev_number = rev_number1 + '.' + rev_number2
    return(rev_number)

print('\nПервое число наоборот:', revers(first_number))
print('Второе число наоборот:', revers(second_number))
print('Сумма:', float(revers(first_number)) + float(revers(second_number)))