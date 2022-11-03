n = int(input())
word_list = []
for _ in range(n) :
    word = input()
    word_list.append(list(map(str, word)))
word_list.sort()
print(word_list)