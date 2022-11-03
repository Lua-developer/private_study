import copy
score_list = []
for _ in range(10) :
    score = int(input())
    score_list.append(score)
answer = 0
for i in range(10) :
    # 이전 계산 값 저장
    before_answer = copy.deepcopy(answer)
    # 값을 더함
    answer += score_list[i]
    # 만약 answer가 100보다 같거나 크면 계산전 값과 계산 후 값을 비교
    if answer >= 100 :
        # 계산 전 값 <- 100보다 작으므로 100에다가 이전 값을 뺀다.
        before = 100 - before_answer
        # 계산 후 값 <- 100보다 크므로 100을 빼준다.
        after_answer = answer - 100
        # 두 값을 비교
        if before < after_answer :
            print(before_answer)
            break
        else :
            print(answer)
            break
if answer < 100 :
    print(answer)