maximum = 0
index = 0
for i in range(9) :
    inputs = int(input())
    if inputs > maximum :
        maximum = inputs
        index = i
print(maximum)
print(index+1)