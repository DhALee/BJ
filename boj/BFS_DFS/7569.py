from collections import deque
import pprint
import sys


m, n, h = map(int, input().split())
tomato = [[] for i in range(h)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 1]
seed = deque()

# pprint.pprint(tomato)
# sys.exit()

for i in range(h):
    for _ in range(n):
        tomato[i].append(list(map(int, input().split())))

# pprint.pprint(tomato)
# sys.exit()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                seed.append([x, y, z])

result = 0
trial = len(seed)
while seed:
    cur = seed.popleft()
    trial -= 1
    x, y, z = cur[0], cur[1], cur[2]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if tomato[z][nx][ny] == 0:
                tomato[z][nx][ny] = 1
                seed.append([nx, ny, z])
    for i in range(2):
        nz = z + dz[i]
        if 0 <= nz < h:
            if tomato[nz][x][y] == 0:
                tomato[nz][x][y] = 1
                seed.append([x, y, nz])
    if trial == 0:
        result += 1
        trial = len(seed)
        # print(trial, end=' ')
result -= 1

# go = [[[one for one in one_d] for one_d in two_d] for two_d in tomato]
# for i in go:
#     print(i)

# if any([[0 in one_d for one_d in two_d] for two_d in tomato]): # to check if list has 0
#         result = -1

for i in range(h):
    if any(0 in two_d for two_d in tomato[i]): # to check if list has 0
        result = -1

print(result)