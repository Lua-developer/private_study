N = int(input())
array = list()

for _ in range(N) :
    temp = int(input())
    array.append(temp)
array.sort(reverse=True)
print(array)