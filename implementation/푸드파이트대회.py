from copy import deepcopy
def solution(food):
    answer = ''
    # food[0] = 물
    # food[1:] 음식 양
    # 만약 음식이 홀수개면 짝수개로 사용 ( -1)
    for index in range(1, len(food)) :
        # 음식이 홀수개면 1개를 뺀다.
        if food[index] % 2 == 1 :
            food[index] = food[index] - 1
        for _ in range(food[index] // 2) :
            answer += "{}".format(index)
    temp = deepcopy(answer)
    answer += '0'
    temp = list(temp)
    temp.reverse()
    for a in temp :
        answer += a
    return answer