from collections import deque
import sys

dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]

def knight(start, goal, chess):
    if (start[0] == goal[0]) and (start[1] == goal[1]):
        return 0
    queue = deque([start])
    size = len(chess)
    while queue:
        cur = queue.popleft()
        x, y = cur[0], cur[1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # if (0 <= nx < size) and (0 <= ny < size) and ([nx, ny] not in queue) and (chess[nx][ny] == 0): # not in -> time excess
            if (0 <= nx < size) and (0 <= ny < size) and (chess[nx][ny] == 0):
                chess[nx][ny] = chess[x][y] + 1
                queue.append([nx, ny])
                if (nx == goal[0]) and (ny == goal[1]):
                    return chess[nx][ny]

    # return chess[goal[0]][goal[1]]


case = int(sys.stdin.readline())
result = []

for _ in range(case):
    start = []
    goal = []
    chess = []

    l = int(sys.stdin.readline())
    # chess = [[0] * l] * l --------------> NEVER USE THIS 2d array format
    chess = [[0 for _ in range(l)] for _ in range(l)]
    start = list(map(int, sys.stdin.readline().split()))
    goal = list(map(int, sys.stdin.readline().split()))
    
    result.append(knight(start, goal, chess))

for i in result:
    print(i)