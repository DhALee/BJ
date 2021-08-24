from collections import deque

n, k = map(int, input().split())
graph = [0] * 100001

def bfs(n, k):
    if n == k:
        return 0
    queue = deque([n])
    while queue:
        cur = queue.popleft()
        dn = [cur, -1, 1]
        for i in range(3):
            nn = cur + dn[i]
            # if (0 <= nn <= 100000) and nn not in queue and nn != n: # not in -> time excess
            if (0 <= nn <= 100000) and nn != n:
                if graph[nn] == 0:
                    graph[nn] = graph[cur] + 1
                    queue.append(nn)
                    if nn == k:
                        return graph[nn]

print(bfs(n, k))