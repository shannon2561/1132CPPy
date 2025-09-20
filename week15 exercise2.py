Input = input().split()

number=[]
for n in Input:
    N=int(n)
    number.append(N)

categories=[]
divisible_dict={}
for N in number:
    divisible_list=[]
    divisor=2
    while divisor <= N:
        if N % divisor == 0:
            divisible_list.append(divisor)
        divisor+=1
        # print("is_prime", is_prime)
        # print("divisor:", divisor)
    
    divisible_dict[N] = divisible_list

# print(categories)

# divisible_list2=list(divisible_dict)
# print(divisible_dict)

A = number[0]
divisible_A = divisible_dict[A]
# print(divisible_dict[A])
B = number[1]
divisible_B = divisible_dict[B]
# print(divisible_dict[B])


# set: intersection = set(divisible_dict[A]) & set(divisible_dict[B])
CD = [x for x in divisible_dict[A] if x in divisible_dict[B]]
# CD = [x for x in divisible_A if x in divisible_B]
# print(CD)
try:
    GCD = max(CD)
except ValueError:
    GCD = None

if GCD == None:
    LCM = A * B
else:
    LCM = int(A * B / GCD)

print(LCM)




#-------------------------------------------------------------
# CD = []
# for divisible_dict[A] in divisible_dict[B]:
#     CD.append()

# GCD = 


#--------------------------------------------------------------

# if categories == [True, True]:
#     LCM = A * B

# else:
