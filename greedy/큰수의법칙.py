# n은 숫자 개수, m은 몇번 계산 할 것인가, k는 같은 인덱스 값을 중복해서 사용할 수 있는 횟수
n, m, k = map(int, input().split())
# 리스트 생성
# N개의 수를 입력받는다.
temp = list(map(int, input().split()))
# 그리디 문제는 항상 정렬 후 푸는게 핵심
temp.sort()
# 문제 접근
# 총 m번 연산, 리스트에서 가장 큰 값인 array[0]을 k번 연산한 후 두번째 큰 값인 array[1]을 한번 더한다.
# 이 계산을 m이 될때까지 반복
answer = 0
count = 0
for _ in range(m) :
    # k 횟수 계산
    # 만약 k번 큰 수를 계산하였으면, 2번째 큰 값을 더하고 count를 초기화
    if k == count :
        answer += temp[1]
        count = 0
    answer += temp[0]
print(answer)