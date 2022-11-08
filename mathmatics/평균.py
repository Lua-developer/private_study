def isPrime(num) :
    for seq in range(2, num-1) :
        if num % seq == 0 :
            return False
    return True

n = int(input())
m = int(input())

sum = 0
min = 20000
for number in range(n, m, 1) :
    # 소수는 2부터 x-1 까지 나누었을때 나머지가 0이 아닌 값
    if number <= 1 :
        continue
    result = isPrime(number)
    if result == True :
        if min > number :
            min = number
        sum += number
if sum == 0 :
    print("-1")
else :
    print(sum) 
    print(min)