#apple,welcome,banana,cat,archive,once,australia,co,abc

input1=str(input())
#input1="apple,welcome,banana,cat,archive,once,australia,co,abc"
# input1="apple,archive,australia,abc"
list1=input1.split(",")
# print(len(list1))
#dict1={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
dict2={}



for word in list1:
    first_letter = word[0] 
    if first_letter not in dict2:  
        dict2[first_letter] = []  
    dict2[first_letter].append(word)  

#print(dict2)

while True:
    input2=input()
    first_let=input2[0]
    if input2=="#":
        break
    elif input2[0] in dict2:
        for i in range(len(dict2[first_let])):
            #if dict2[first_let][i]==input2:
            if sorted(dict2[first_let])[i]==input2:
                print(input2[0].capitalize(),i+1)

                #print(str(input2[0].capitalize())+" "+str(i+1))
    else:
        print("NOT FOUND")


# pos=0
# for i in range(len(list1)):
#     if dict1[list1[i][0]]==0:
#         pos+=1
#         dicta[list1[i]]=pos
#         #dicta={list1[i]:pos}

#     # print(list1[i])
#     # print(list1[i][0]) #字串[0]是字串的第一個字元
#     # #for j in range():
#     # print(dict1[list1[i][0]])
# print(dicta)