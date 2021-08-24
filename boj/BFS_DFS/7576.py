from collections import deque


m, n = map(int, input().split())
tomato = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
seed = deque()

for _ in range(n):
    tomato.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        if tomato[x][y] == 1:
            seed.append([x, y])

result = 0
trial = len(seed)
while seed:
    cur = seed.popleft()
    trial -= 1
    x, y = cur[0], cur[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                seed.append([nx, ny])
    if trial == 0:
        result += 1
        trial = len(seed)
        # print(trial, end=' ')
result -= 1


if any(0 in one for one in tomato): # to check if list has 0
    result = -1

print(result)
# print(tomato)