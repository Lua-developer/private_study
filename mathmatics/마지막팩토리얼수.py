from math import factorial

n = int(input())

result = factorial(n)
L_result = list(str(result))
L_result.reverse()
print(L_result)
for index in range(len(L_result)) :
    if L_result[index] == '0' :
        continue
    print(L_result[index])
    break