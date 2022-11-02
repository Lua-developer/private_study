# 문자 입력 받기
sentences = list(input())
# 알파벳 리스트
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_list = list()
#print(len(alpha))
# 알파벳 개수만큼 -1를 매핑
for i in range(len(alpha)) :
    alpha_list.append(-1)
for i in range(len(sentences)) :
    for k in range(len(alpha)) :
        # -1인 경우
        if sentences[i] == alpha[k] :
            if alpha_list[k] == -1 :
                alpha_list[k] = i
for i in range(len(alpha_list)) :
    print(alpha_list[i], end=" ")
#print(alpha_list)