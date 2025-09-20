# 17 mins

words = input().split(",")
words_dict = {}
for word in words:
    if word[0] in words_dict.keys():
        # print("word[0] is", word[0])
        words_dict[word[0]].append(word)
        words_dict[word[0]] = sorted(words_dict[word[0]])
    else:
        # print("add", word[0])
        words_dict[word[0]] = [word]

# print(words_dict)

while True:
    searching = input()
    if searching == "#":
        break
    else:
        if searching[0] in words_dict.keys():
            if searching in words_dict[searching[0]]:
                alphabet = searching[0]
                position = words_dict[searching[0]].index(searching)
                print(alphabet.upper(), position+1)
            else:
                print("NOT FOUND")
        else:
            print("NOT FOUND")

# admc,kwkx,lcoe,ksow,lcpe,lose,kxoe