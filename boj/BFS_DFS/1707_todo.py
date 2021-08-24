### NOT FINISHED

from collections import deque
import sys

input = sys.stdin.readline()
k = int(input)

for _ in range(k):
    v, e = map(int, input.split())
    graph = {}
    for _ in range(e):
        if v in graph:
            graph[v].append(e)
        else:
            graph[v] = [e]
        
        if e in graph:
            graph[e].append(v)
        else:
            graph[e] = [v]