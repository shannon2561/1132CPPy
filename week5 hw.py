# Number_of_customers=int(input())
# Name=str(input(""))

Num=int(input())

for N in range(1,Num+1):
    Name=str(input())
    Item=int(input())
    print("Customer:",Name)
    print("Number of Items:",Item)
    print("Order Details:")
            
    Count=0
    Total=0
    for i in range(1,Item+1):
        Input1=str(input())
        List1=Input1.split(";") #string
        #List1=[str(input()),int(input()),float(input()),str(input())]

        List1[1]=int(List1[1])

        List1[2]=float(List1[2])
        Price=f"{List1[2]:.2f}" #string
        List1[2]=float(Price)

        if List1[3]=="NONE":
            Discount=0
        else:
            Discount=int(List1[3].replace("DISC",""))
        # print(List1)
        # print(Discount)
        List1[3]=Discount

        Subtotal=List1[1]*List1[2]*(1-Discount/100)
        Subtotal=f"{Subtotal:.2f}"
    
        Count+=1
        print(str(Count)+".",List1[0],"-","Quantity:",str(List1[1])+",","Unit Price:",Price,"TWD,","Subtotal:",Subtotal,"TWD")
        Subtotal=float(Subtotal)
        Total=Total+Subtotal
        
    Total=f"{Total:.2f}"
    print("Total Cost:",Total,"TWD")
    Total=float(Total)

    if N!=Num:
        print()

# print(%.2f % List1[2])        
# split(DISC10)