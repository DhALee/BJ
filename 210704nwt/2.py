from collections import deque

def bfs(grpah, x, y):
    queue = deque()
    queue.append((x, y))
    visited = set([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if (nx, ny) not in visited:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))
                visited.add((nx, ny))

    return graph[n-1][m-1]

graph = [[1, 8, 3, 2], [7, 4, 6, 5]]
n, m = len(graph), len(graph[0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(graph, 0, 0))
# print(bfs2(graph, (0, 0)))