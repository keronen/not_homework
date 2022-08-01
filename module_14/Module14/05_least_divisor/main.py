def numb():
    number = int(input('введите натуральное число больше 1: '))
    if number <= 1:
        numb()
    return(number)

y = numb()
for i in range(2, y + 1):
    if y % i == 0:
        print('Наименьший делитель, отличный от единицы:', i)
        break
