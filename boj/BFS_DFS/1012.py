"""
import sys
sys.setrecursionlimit(10**6) # change the maximum recursive depth for dfs version

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x -1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

T = int(input())

result_list = []
for _ in range(T):
    result = 0
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)] # m is column(width), n is row(height)
    for _ in range(k):
        x, y = map(int, input().split()) # (x, y) 2d coordinate system
        graph[y][x] = 1 # x and y literally means 2d coordinate system whice is inverse with 2d array
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    result_list.append(result)

for i in result_list:
    print(i)
"""
# bfs version
from collections import deque

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result_list = []
for _ in range(T):
    result = 0
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)] # m is column(width), n is row(height)
    for _ in range(k):
        x, y = map(int, input().split()) # (x, y) 2d coordinate system
        graph[y][x] = 1 # x and y literally means 2d coordinate system whice is inverse with 2d array

    count = 0

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                count += 1
                queue = deque([[x, y]])
                while queue:
                    cur = queue.popleft()
                    # print(cur)
                    cur_x, cur_y = cur[0], cur[1]
                    graph[cur_x][cur_y] = 0
                    for i in range(4):
                        if (0 <= cur_x + dx[i] < n) and (0 <= cur_y + dy[i] < m):
                            if (graph[cur_x + dx[i]][cur_y + dy[i]]) and ([cur_x + dx[i], cur_y + dy[i]] not in queue):
                                queue.append([cur_x + dx[i], cur_y + dy[i]])
    print(count)