nums = input().split()
nums_int = []

for n in nums:
    n = int(n)
    nums_int.append(n)

nums_sorted = sorted(nums_int)
# print(nums_int)
# print(nums_sorted)

N=len(nums_int)

# print(nums_int != nums_sorted)

swap=0
while nums_int != nums_sorted:
    # round=0
    for i in range(N-1):
        # round+=1
        # print("Round", round)
        # print("swap:", swap)

        if nums_int[i] <= nums_int[i+1]:
            pass
        else:
            swap+=1
            pre_n = nums_int[i]
            pro_n = nums_int[i+1]
            nums_int[i]=pro_n
            nums_int[i+1]=pre_n

        #     print("小：", pro_n)
        #     print("大：", pre_n) 

        # print(nums_int)
        # print()

strs_list=[]
for ints in nums_int:
    strs = str(ints)
    strs_list.append(strs)

print(" ".join(strs_list))
print("Swap:", swap)




    # if i <= i+1:
    #     pass
    # # print(i)
    # # print(i+1)

# swap = 0
# for N in nums_int:
#     for next_N in nums_int:
#         if N <= next_N:
#             pass
#         else:
#             swap+=1


#------------------------------------------------
# .join() 是 Python 字串（str）的一個方法，通常用來
# 「將一個可迭代的字串序列（例如：list、tuple）用特定的分隔符號組合成一個新的字串」。
# '分隔符號'.join(可迭代物件)
# ex. 
# words = ['I', 'love', 'Python']
# sentence = ' '.join(words)
# print(sentence)