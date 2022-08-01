# a = int(input('A: '))
# b = int(input('B: '))
# #
# list_a = [u for u in range(a, b + 1) if u % 2 == 0]
# # list_b = [u ** 2 for u in range(a, b + 1)]
# #
# print(list_a)
# print(list_b)
#
# a = input('A: ')
# b = input('B: ')
#
# list_a = [u * 2 for u in list(a)]
# list_b = [u + b for u in list_a]
#
# print(list_a)
# print(list_b)
#
# def price_increase(percent, price):
#     return price * (1 + percent / 100)
#
# list_price = [float(input('price: ')) for _ in range(5)]
# first_increase = int(input('increase for first year: '))
# second_increase = int(input('increase for second year: '))
#
# first_inrcease = [price_increase(first_increase, i_price) for i_price in list_price]
# second_inrcease = [price_increase(second_increase, i_price) for i_price in list_price]
# #
# # print(round(sum(list_price), 2), round(sum(first_inrcease), 2), round(sum(second_inrcease), 2))
#
#
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_prices = [(0 if i_price < 0
#                else i_price)
#               for i_price in original_prices]
# print(new_prices)
# import random
#
#
# first_branch = [random.randint(30, 60) for _ in range(10)]
# second_branch = [random.randint(50, 80)  for _ in range(10)]
# third_branch =[('died' if first_branch[random.randint(0, 9)]
#                            + second_branch[random.randint(0, 9)]
#                            > 100 else 'alive') for _ in range(10)]
# # third_branch =[('died' if first_branch[i]
# #                            + second_branch[i]
# #                            > 100 else 'alive') for i in range(10)]
#
# print(first_branch)
# print(second_branch)
# print(third_branch)

# original_prices = [-12, 3, 5, -2, 1]
# new_prices = [(0 if i < 0 else i) for i in original_prices]
#
# # new_prices = original_prices[:]
# #
# # for i in range(len(original_prices)):
# #
# #     if new_prices[i] < 0:
# #
# #         new_prices[i] = 0
#
# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
#
# import random
#
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# # print(nums[:5])
# # print(nums[:len(nums) - 2])
# # print(nums[::2])
# # print(nums[1::2])
# # print(nums[::-1])
# # print(nums[6:2:-2])
# n = len(nums)
# b = random.randint(0, n - 1)
# a = random.randint(0, b - 1)
# nums[a:b] = []
# print(nums)