# for i in range(1,100):
#     if i%2==0:
#         print(i,"is an even number")
#     else:
#         print(i,"is an odd number.")

# if type(a) != int:

a=int(input())

if a==1:
    print("1 is not a prime number.")

count=0
for i in range(a,1,-1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print("Largest Prime Number:",i)
        count+=1
    if count==1:
        break
