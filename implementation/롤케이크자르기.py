def solution(topping):
    answer = 0
    for index in range(1, len(topping)) :
        # 오빠꺼 동생꺼
        topping_1 = set(topping[:index])
        topping_2 = set(topping[index:])
        if len(topping_1) == len(topping_2) :
            answer += 1
    return answer