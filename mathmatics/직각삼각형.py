# 입력
input_list = []
while True :
    n, m, k = map(int, input().split())
    input_list.append((n, m, k))
    # 종료조건
    if n == 0 and m == 0 and k == 0 :
        break
# 0, 0, 0은 제외
for size in range(len(input_list) - 1) :
    # 가장 긴 변이 빗변
    h = max(input_list[size])
    sum = 0
    for i in range(3) :
        if input_list[size][i] == h :
            continue
        sum += input_list[size][i] ** 2
    if pow(h, 2) == sum :
        print('right')
    else :
        print('wrong')