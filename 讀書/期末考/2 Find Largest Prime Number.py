#1h 13 mins

N = int(input())
if N == 1:
    print("1 is not a prime number.")
# else:
#     prime = None
#     for n in range(2, N+1):
#         print("n:", n)
#         for div in range(2, n-1):
#             print("div:", div)
#             if n % div == 0:
#                 break
#             else:
#                 prime = n

# print(f"Largest Prime Number: {prime}")

else:
    largest_prime = 2
    for n in range(2, N+1):
        # print("n=", n)
        for div in range(2, n+1):
            is_prime = True
            # print("div", div)
            if n % div == 0 and n != div:
                is_prime = False
                # print(f"{n} is not prime")
                # print("now:", largest_prime)
                # print()
                break
            # else:
                # print(f"{n} is prime")
                # print("now:", largest_prime)
                # print()
            
            if div == n and is_prime == True:
                largest_prime = n
            

    print(f"Largest Prime Number: {largest_prime}")



#method2
N = int(input())
if N == 1:
    print("1 is not a prime number.")

else:
    for n in range(N, 2, -1):
        for div in range(2, n):
            if n % div == 0:
                break
        else:
            print(f"Largest Prime Number: {n}")
            break