from collections import deque

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    # 방문처리
    graph[y][x] = 0
    # 큐가 빌때까지 반복
    while queue :
        ax, ay = queue.popleft()
        for index in range(4) :
            dx = ax + nx[index]
            dy = ay + ny[index]
            if dx < 0 or dx >= m or dy < 0 or dy >= n :
                continue
            if graph[dy][dx] == 1 :
                # 방문처리
                graph[dy][dx] = 0
                queue.append((dx, dy))

# 좌, 우, 상, 하
nx = [-1, 1, 0, 0]
ny = [0, 0, 1, -1]
t = int(input())
for _ in range(t) :
    count = 0
    n, m, k = map(int, input().split())
    # 그래프 생성
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k) :
        y, x = map(int, input().split())
        graph[y][x] = 1

    for y in range(n) :
        for x in range(m) :
            if graph[y][x] == 0 :
                continue
            else :
                bfs(x,y)
                count += 1
    print(count)