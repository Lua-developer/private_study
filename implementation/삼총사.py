# 조합 문제
# 중복되지 않은 3개의 순열을 사용하여 구한다.
from itertools import combinations
def solution(number):
    answer = 0
    num = list(combinations(number, 3))
    for i in range(len(num)) :
        if sum(num[i]) == 0 :
            answer += 1
    return answer