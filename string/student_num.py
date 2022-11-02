n = int(input())
student_id = list()
answer = 0
# 모든 학생의 학번 길이는 같다고 가정
for i in range(n) :
    student_id.append(input())
length = len(student_id[0])
# 첫째자리 부터 중복 여부 체크
for i in range(1, length) :
    # 쪼갠 문자열을 임시로 저장, 중복을 제외해야 하므로 set으로 세팅
    temp_list = set()
    # n개의 문자열에 대해 쪼갠다.
    for k in student_id :
        temp_list.add(k[-i:])
    # 중복되지 않은 학번의 개수가 n과 동일하면 최소의 값이 나옴
    if len(temp_list) == n :
        answer = i
        break
print(answer)