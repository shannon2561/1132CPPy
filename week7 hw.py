Input1=input()
List1=Input1.split(" ")
List1=list(map(int, List1))
Days=len(List1)

#6
Max=List1[0]
Min=List1[0]
Profit=0
#count=0
for i in range(Days):
    #count+=1
    #print(count)
    if List1[i]<Min:
        Min=List1[i]
        Max=List1[i]
        # print("List1[i]<Min:")
        # print("Min=",Min)
        # print("Max=",Max)

    elif List1[i]>Max:
        Max=List1[i]
        # print("List1[i]>Max:")
        # print("Min=",Min)
        # print("Max=",Max)
    Profit=max(Profit,Max-Min) 
    #print("Min=",Min)
    #print("Max=",Max)
print(Profit)
    



#5 #Wrong
# Max=List1[0]
# Min=List1[0]
# Profit=Max-Min
# List2=[Profit]
# count=0
# for i in range(1,Days):
#     count+=1
#     print(count)
#     if List1[i]<Min:
#         Min=List1[i]
#         Profit=Max-Min
#         List2.append(Profit)
#         # print("List1[i]<Min:")
#         # print("Min=",Min)
#         # print("Max=",Max)
#         print(Profit)

#     elif List1[i]>Max:
#         Max=List1[i]
#         Profit=Max-Min
#         # print("List1[i]>Max:")
#         # print("Min=",Min)
#         # print("Max=",Max)
#         print(Profit)
    
#     #print("Min=",Min)
#     #print("Max=",Max)

# print(List2)
# Best_Price=max(List2)
# print(Best_Price)



#4 #Wrong
# Max=List1[0]
# Min=List1[0]
# Profit=Max-Min
# List2=[Profit]
# count=0
# for i in range(1,Days):
#     count+=1
#     print(count)
#     if List1[i]>Max:
#         Max=List1[i]
    
#     if List1[i]<Min:
#         Min=List1[i]
#         Profit=Max-Min
#         List2.append(Profit)
#         print("Profit:",List2)

# Best_Profit=max(List2)
# if Best_Profit==0:
#     print("0")
# else:
#     print(Best_Profit)   



#3 #Partial Accepted
# Max=List1[0]
# Min=List1[0]
# Profit=Max-Min
# count=0
# for i in range(1,Days):
#     count+=1
#     print(count)
#     if List1[i]<Min:
#         New_Min=List1[i]
#         New_Profit=Max-New_Min
#         if New_Profit>Profit:
#             Profit=New_Profit
#             Min=New_Min
#             Max=New_Min
#         print("Min:",Min)
#         print("Profit:",Profit)

#     if List1[i]>Max:
#         New_Max=List1[i]
#         New_Profit=New_Max-Min
#         if New_Profit>Profit:
#             Profit=New_Profit
#             Max=New_Max
#         print("Max:",Max)
#         print("Profit:",Profit)

# if Max==Min:
#     print("0")
# else:
#     print(Profit)



#2 #Partial Accepted
# Max=List1[0]
# Min=List1[0]
# #count=0
# for i in range(Days):
#     #count+=1
#     #print(count)
#     if List1[i]<Min:
#         Min=List1[i]
#         Max=List1[i]
#         # print("List1[i]<Min:")
#         # print("Min=",Min)
#         # print("Max=",Max)

#     elif List1[i]>Max:
#         Max=List1[i]
#         # print("List1[i]>Max:")
#         # print("Min=",Min)
#         # print("Max=",Max)
    
#     #print("Min=",Min)
#     #print("Max=",Max)


# Price=Max-Min
# Max_index=List1.index(Max)
# Min_index=List1.index(Min)

# if Max_index>Min_index:
#     print(Price)
# else:
#     print("0")



#1
# Max=List1[0]
# Min=List1[0]
# for i in range(Days-1):
#     if List1[i]<List1[i+1]:
#         Max=List1[i+1]
#         print("Max=",Max)
#     elif Min>List1[i+1]:
#         Min=List1[i+1]
#         print("Min=",Min)

# Price=int(Max)-int(Min)
# Max_index=List1.index(Max)
# Min_index=List1.index(Min)

# if Max_index>Min_index:
#     print(Price)
# else:
#     print("0")