def Dirty_Map(x,y):
    if x<0 or y<0 or x>=Dorm or y>=Dorm:
        return
    if Dorm_Map[x][y]==".":
        return
    if Dorm_Map[x][y]=="#":
        Dorm_Map[x][y]="."    
        Dirty_Map(x+1,y)
        Dirty_Map(x-1,y)
        Dirty_Map(x,y+1)
        Dirty_Map(x,y-1)

Cases=int(input())
for N in range(Cases):
    Dorm=int(input())
    Dorm_Map=[]
    for n in range(Dorm):
        Row=input()
        Dorm_Map.append(list(Row))
    
    Dirty_Zone=0
    for x in range(Dorm):
        for y in range(Dorm):
            #Dirty_Zone=Dirty_Map(x,y)
            if Dorm_Map[x][y]=="#":
                Dirty_Zone+=1
                Dirty_Map(x, y)

    print(Dirty_Zone)


#-------------------------------------------

#  def Dirty_Map(x,y):
#     for x in range(Dorm):
#         for y in range(Dorm):
#             if Dorm_Map[x][y]=="#":
#                 Dorm_Map[x][y]="Dirty"


#--------------------------------------

# def Dirty_Index(Row):
#     Row=input()
#     result=[]
#     for i in range(len(Row)):
#         if Row[i]=="#":
#             result.append(i)
#     return result
# # x=Dirty_Index()
# # print(x)

# # def Dirty():
# #     Dirty_Zone=0
# #     for j in range(dorm):
# #         if set(Dirty_Index(j))&set(Dirty_Index(j+1)):
            
# #         else:
# #             Dirty_Zone+=1
            
# def Dirty():
#     Dirty_Zone=0
#     if set(Dirty_Index)&set(Dirty_Index):
        
#     else:
#         Dirty_Zone+=1


# #1
# cases=int(input())
# for N in range(cases):
#     dorm=int(input())
#     for _ in range(dorm):
        
# #     for n in range(dorm):
# #         print(Dirty)
            


#------------------------------------------


# cases=int(input())

# def Index_Dirty(List_Dirty,y):
#     for i in range(len(List1)):
#         if List1[i]=="#":
#             List_Dirty.append(i)
#     return y
    

# for N in range(cases):
#     List1=input().split
#     x=Index_Dirty

# def Dirty(Dirty_Tile,Dirty_Zone):
#     Dirty_Tile=index


#-------------------------------------------
    
        # Row=input()
        # if Dirty_Index not in 
        # for j in range(len(Row)):
        #     if Row[j]=="#":
        #         Dirty_Index.append(j)


#     for i in range(dorm):
#         Input1=input()
#         List1=Input1.split("")
#         List_Dirty=[]
#         for j in range(len(List1)):
#             if List1[j]=="#":
#                 List_Dirty.append(j)
