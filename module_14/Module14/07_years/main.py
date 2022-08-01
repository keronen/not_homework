first_year = int(input('введите первый год: '))
second_year = int(input('введите второй год: '))
print('Годы от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')
count2 = 0

for year in range(first_year, second_year + 1):
    for i in range(10):
        count = 0
        for digit in str(year):
            if int(digit) == i:
                count += 1
        if count == 3:
            print(year)
            count2 += 1

if count2 == 0:
    print('no')

