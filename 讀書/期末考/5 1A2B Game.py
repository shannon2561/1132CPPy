from itertools import permutations

possible = []
while True:
    Input = input()
    if Input == "q":
        break
    else:
        Input1 = Input.split(" -> ")
        guess = Input1[0].split(" ")
        ori_0 = guess[0]
        ori_1 = guess[1]
        ori_2 = guess[2]
        ori_3 = guess[3]
        result = Input1[1]
        a = int(result[0])
        b = int(result[2])
        if a == 4:
            possible.append(guess)
            break

        elif a == 3:
            for i in range(1, 10):
                guess[0] = i
                possible.append(guess)
            guess[0] = ori_0
            for i in range(1, 10):
                guess[1] = i
                possible.append(guess)
            guess[1] = ori_1
            for i in range(1, 10):
                guess[2] = i
                possible.append(guess)
            guess[2] = ori_2
            for i in range(1, 10):
                guess[3] = i
                possible.append(guess)
            guess[3] = ori_3
        
        elif a == 2:
            