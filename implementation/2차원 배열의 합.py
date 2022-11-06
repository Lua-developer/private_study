n, m = map(int, input().split())
# 미리 0을 채운 리스트를 만들고
# 1,1 부터 값을 넣는 방식
matrix = []
for y in range(1, n + 1) :
    temp = list(map(int, input().split()))
    matrix.append(temp)
# 모든 좌표에 -1, -1
k = int(input())

for index in range(k) :
    answer = 0
    x, y, w, h = map(int, input().split())
    x, y, w, h = x - 1, y - 1, w - 1, h - 1
    for y_num in range(x, w) :
        for x_num in range(y, h) :
            answer += matrix[x_num][y_num]
            print(answer)