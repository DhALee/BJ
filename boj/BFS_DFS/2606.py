num_of_computer = int(input())
num_of_edge = int(input())
start = 1

graph = {}
for _ in range(num_of_edge):
    key, value = map(int, input().split())
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]
    
    if value in graph:
        graph[value].append(key)
    else:
        graph[value] = [key]
# print(graph)

visited = []
def dfs(graph, start):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # print(node, end=' ')
            graph[node].sort(reverse=True)
            stack.extend(graph[node])

dfs(graph, start)
result = len(visited) - 1
print(result)