import sys

def recusion(count, n) :
    # 1의 자리가 될때까지 반복
    if len(n) > 1 :
        count += 1
        n_split = list(map(int, str(n)))
        print(n_split)
        n_sum = sum(n_split)
        recusion(count ,str(n_sum))
    # 한자리 수가 되었을때
    else :
        n = int(n)
        # 만약 3의 배수면
        print(count)
        if n % 3 == 0 :
            print(count)
            print("YES")
        else :
            print(count)
            print("NO")
count = 0
n = input()
recusion(count, n)