
number = int(input('пожалуйста введите целое положительное число: '))
while number <= 0:
    number = int(input('еще раз: пожалуйста введите целое положительное число: '))

def summ(number):
    summ = 0
    while number != 0:
        summ += number % 10
        number //= 10
    return(summ)

def counter(number):
    counter = 0
    while number != 0:
        counter += 1
        number //= 10
    return (counter)

print('сумма чисел:', summ(number))
print('Количество цифр в числе:', counter(number))
print('Разность суммы и количества цифр:', summ(number) - counter(number))
