n = int(input())
book_list = {}
name_list = []
for _ in range(n) :
    name = input()
    if name in book_list :
        book_list[name] += 1
    else :
        book_list[name] = 1
max_value = max(book_list.values())
for name, size in book_list.items() :
    if size == max_value :
        name_list.append(name)
name_list.sort()
print(name_list[0])