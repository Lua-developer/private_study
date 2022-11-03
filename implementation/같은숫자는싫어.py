def solution(arr):
    answer = []
    # 미리 첫번째 값을 answer 리스트에 추가한다.
    answer.append(arr[0])
    # 첫번째 값이 있으므로 전체 리스트를 순회할때 1번 값부터 순회
    for i in range(1, len(arr)) :
        # 만약 answer의 마지막 값이 현재 위치의 arr 값과 동일하면 그냥 넘어간다.
        if answer[-1] == arr[i] :
            continue
        # 아니라면 answer에 추가한다.
        answer.append(arr[i])
    return answer