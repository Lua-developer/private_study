pay = 1000 - int(input())
coin_type = [500, 100, 50, 10, 5, 1]
answer = 0
for coin in coin_type :
    # pay < coin
    if pay // coin == 0 :
        continue
    answer += pay // coin
    pay = pay % coin
print(answer)