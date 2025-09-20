# print(len("abc")==3)

# print("abcd"[2:]== "cd")

# print(round(3.14159,3))

# print([1, 2, 3, 4][1:3])
# print([1, 2, 3, 4][1:3][1])

# x=y=0
# print(x == x)
# print(type(x == y))

# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print('L3 =', L3)
# L1.extend(L2)
# print('L1 =', L1)
# L1.append(L2)
# print('L1 =',L1)

# def doSomething(x, func):
#     return func(x)


# monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
# print('The third month is ' + monthNumbers[3])
# dist = monthNumbers['Apr'] - monthNumbers['Jan']
# print('Apr and Jan are', dist, 'months apart')


# monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
# keys = []
# for e in monthNumbers:
#     keys.append(str(e))
# print(keys)
# keys.sort()
# print(keys)

# birthStones = {'Jan':'Garnet', 'Feb':'Amethysgt', 'Mar':'Acquamarine', 'Apr':'Diamond', 'May':'Emerald'}
# months = birthStones.keys()
# print(months)
# birthStones['June'] = 'Pearl'
# print(months)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict['a'])  # Output: 1

# # nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# # num_labels=[]
# # for num in nums:
# #     if num%2==0:
# #         num_labels.append("even")
# #     else:
# #         num_labels.append("odd")

# # print(num_labels)

# #input("Press Enter your name:")

# input1=input().split(";")
# print(input1)

# a=[1,2,3,4,5,6]
# print(a[:3])'



phone_numbers={"Zehra": 123, "Shannon": 456}
print(phone_numbers.keys())
print(phone_numbers["Shannon"])
print(list(phone_numbers.values()))
print(phone_numbers.values())
print(phone_numbers.items())

phone_numbers["Shannon"] = 789
del phone_numbers["Zehra"]

for k, v in phone_numbers.items():
    print(k, v)

for key in phone_numbers.keys():
    print(key)



