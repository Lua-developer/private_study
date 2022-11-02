n = int(input())
# 문자열을 받기 위한 리스트
sentences = []
# N개의 문자열을 받는다.
for i in range(n) :
    temp = input()
    sentences.append(temp)
# 문자열에 대해 뒤집기 시작
for sentense in sentences :
    # 공백 단위로 문자를 쪼개기
    words = sentense.split()
    # 쪼갠 문자 리스트에서 문자를 뒤집어 출력 한다.
    for word in words :
        print(word[::-1], end=" ")
    print("")