from collections import deque

# n is vertex, m is edge, v is start
n, m, v = map(int, input().split())

### dictionary version ###
graph_dict = {}
for _ in range(m):
    key, value = map(int, input().split())
    if key in graph_dict:
        graph_dict[key].append(value)
    else:
        graph_dict[key] = [value]

    if value in graph_dict:
        graph_dict[value].append(key)
    else:
        graph_dict[value] = [key]
    
# print(graph_dict)


### list version ###
### Initialize 2d array => [[0 for c in range(#column)] for r in range(#row)]
# graph_list = [[] for _ in range(n + 1)]
# for _ in range(m):
#     i, v = map(int, input().split())
#     graph_list[i].append(v)
#     graph_list[v].append(i)

# print(graph_list)


def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            if node not in graph: # when disconnected node come, keep going
                continue
            graph[node].sort(reverse=True) # to visit from small number node
            stack.extend(graph[node])


def bfs(graph, start):
    visited = []
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            if node not in graph: # when disconnected node come, keep going
                continue
            graph[node].sort() # to visit from small number node
            queue.extend(graph[node])

dfs(graph_dict, v)
print()
bfs(graph_dict, v)