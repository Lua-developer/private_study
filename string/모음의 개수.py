word_list = []
mom = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True :
    word = input()
    list(word)
    if word == '#' :
        break
    word_list.append(word)
for word in word_list :
    count = 0
    word = list(map(str, word))
    for w in word :
        if w in mom :
            count += 1
    print(count)