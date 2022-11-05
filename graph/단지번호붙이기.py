from collections import deque

def bfs(a, b) :
    queue = deque()
    queue.append((a,b))
    matrix[a][b] = 0
    # 방문처리 후 1 추가
    num = 1
    while queue :
        y, x = queue.popleft()
        for index in range(4) :
            nx = x + dx[index]
            ny = y + dy[index]
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            if matrix[ny][nx] == 1 :
                matrix[ny][nx] = 0
                queue.append((ny, nx))
                num += 1
    num_area.append(num)

matrix = []
num_area = []
# 좌, 우, 상, 하
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# 단지 개수
count = 0
n = int(input())
for _ in range(n) :
    matrix.append(list(map(int, input())))

for a in range(n) :
    for b in range(n) :
        if matrix[a][b] == 1 :
            bfs(a, b)
            count += 1
print(count)
num_area.sort()
for num in num_area :
    print(num)