t = int(input())
score_list = []
for index in range(t) :
    score_list.append(list(map(int, input().split())))
for i in range(t) :
    count = 0
    lens = score_list[i][0]
    s_sum = sum(score_list[i][1:])
    s_avg = s_sum // lens
    for k in range(1, lens+1) :
        #print(score_list[i][k])
        if score_list[i][k] > s_avg :
            count += 1
    result = round((count / lens) * 100,3)
    print("{:.3f}%".format(result))