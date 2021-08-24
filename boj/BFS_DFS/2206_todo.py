### NOT FINISHED

from collections import deque

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
breakthrough = False

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        cur = queue.popleft()
        x, y = cur[0], cur[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])
    return graph[n - 1][m - 1]

result = bfs(0, 0)


if result == 0:
    # when breakthrough possible
    if breakthrough:
        print()

    # when no way is possible
    else:
        print(-1)
else:
    print(result + 2) # include start and end point