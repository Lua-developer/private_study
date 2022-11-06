from itertools import combinations

n = int(input())
answer = []
maximum = 0
for lens in range(n) :
    card_list = list(map(int, input().split()))
    result = list(combinations(card_list, 3))
    local_maximum = 0
    # 3개 숫자의 합은 2자리 이상을 넘기지 않으므로 그냥 나머지 연산으로 자릿수를 구한다.
    for card in result :
        temp = sum(card) % 10
        if local_maximum < temp :
            local_maximum = temp
    # 최대값 넣기
    # 1부터 N + 1까지
    answer.append((local_maximum, lens + 1))
answer = sorted(answer, key=lambda x : (-x[0], -x[1]))
print(answer[0][1])