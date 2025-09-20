List0=[0,1,2,3,4,5,6,7,8,9]
# List1= input().split(" ")
List1= ("1 2 3 4 -> 0A1B").split(" ")
# print(List1)
List2=[int(List1[0]),int(List1[1]),int(List1[2]),int(List1[3])]

from itertools import permutations
if List1[5]=="0A0B":
    List3=[x for x in List0 if x not in List2]   #list comprehension
    #print(List3)
    perm1=list(permutations(List3,4))
    print(perm1)

if List1[5]=="0A1B":
    for i in range(4):
        List4=[x for x in List0 if x not in List2]
        pop_value=List2.pop(i)
        print(pop_value)
        List5=[pop_value]+List4
        print(List5)
        List2=[int(List1[0]),int(List1[1]),int(List1[2]),int(List1[3])]
        perm2_1=list(permutations(List5,4))
        perm2=[perm for perm in perm2_1 if perm[i]!=List2[i]]
        print(perm2)
    #     perm2+=perm2_1
    # print(perm2)

if List1[5]=="0A2B":


# while True:
