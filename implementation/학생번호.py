n = int(input())
st_id = []
k = 0
set_st_id = set()
for i in range(n) :
    id = list(map(str, input()))
    st_id.append(id)
# 3부터 문자열 길이 까지 반복
for iter in range(3, len(st_id[0])) :
    for index in range(n) :
        temp = st_id[index][-iter:]
        temp = "".join(temp)
        set_st_id.add(temp)
    if len(set_st_id) == n :
        k = iter
        break
print(k)