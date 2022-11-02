# 밧줄 개수
n = int(input())
array = list()
value = list()
for _ in range(n) :
    # 무게를 받고 list에 추가
    weight = int(input())
    array.append(weight)
array.sort(reverse=True)
for num in range(n) :
    value.append(array[num] * (num+1))
print(max(value))