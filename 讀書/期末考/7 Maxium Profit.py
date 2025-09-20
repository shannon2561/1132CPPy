#1h

Input = input().split()
price = []
for n in Input:
    n = int(n)
    price.append(n)

def cal_max_profit(standard, price_list, profits):
    standard_index = price_list.index(standard)
    for i in range(standard_index, len(price_list)):
        if standard < price_list[i]:
            profit = price_list[i] - standard
            profits.append(profit)
    return profits

max_profits = []
for j in range(len(price)-1):
    max_profits = cal_max_profit(price[j], price, max_profits)

if max_profits != []:
    max_price = max(max_profits)
    print(max_price)
else:
    print(0)

# profit = 0
# Max = 0
# Min = 0
# for i in range(len(price) - 1):
#     if price
#     if_Max = price[i]
#     if_Min = price[i]
#     if profit < if_Max - Min:
#         Max = price[i]
#     if profit < Max - if_Min:
#     if_Max = 0
#     if_Min = 0
#     profit = Max - Min

# profit = 0
# Max = price[0]
# Min = price[0]
# for i in range(len(price) - 1):
#     print("price=", price[i])
#     if price[i] < price[i + 1]:
#         if price[i + 1] - Min > profit:
#             Max = price[i + 1]
#             # if price[i] < Min:
#             #     Min = price[i]
#     if price[i] < Min:
#         if 
#         profit = Max - Min
#     print("Max:", Max)
#     print("Min:", Min)
#     print("Profit:", profit)
#     print()
# print(profit)

# profit = 0
# Max = price[0]
# Min = price[0]
# for i in range(len(price)):
#     if price[i] > Max:
#         if price[i] - Min > profit:
#             Max = price[i]
#     elif price[i] < Min:
#         if Max - price[i] > profit:
#             Min = price[i]
#     else:
#         pass
#     profit = Max - Min
# print(profit)