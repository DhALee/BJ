size = int(input())
graph = []

for _ in range(size):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= size or y < 0 or y >= size:
        return False
    if graph[x][y] == 1:
        global house # add global variable to count num of houses
        house += 1
        graph[x][y] = 0
        dfs(x -1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
house = 0
house_list = []
for i in range(size):
    for j in range(size):
        if dfs(i, j) == True:
            result += 1
            house_list.append(house)
            house = 0 # initialize house to 0 to count new number of houses

print(result)
house_list.sort()
for i in house_list:
    print(i)