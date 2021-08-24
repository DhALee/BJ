n = int(input())
route = input().split()
map = [[0]*n]*n
# R, U, L, D
x, y = 0, 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in route:
    if i == 'R':
        nx = x + dx[0]
        ny = y + dy[0]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            print('Ignore this direction')
            continue 
        x = nx
        y = ny
    elif i == 'U':
        nx = x + dx[1]
        ny = y + dy[1]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            print('Ignore this direction')
            continue
        x = nx
        y = ny
    elif i == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            print('Ignore this direction')
            continue 
        x = nx
        y = ny
    elif i == 'D':
        nx = x + dx[3]
        ny = y + dy[3]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            print('Ignore this direction')
            continue 
        x = nx
        y = ny

print(x+1, y+1)