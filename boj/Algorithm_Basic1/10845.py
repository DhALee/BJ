import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command[:4] == 'push':
        q.append(command[5:])
    elif command == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif command == 'size':
        q: print(len(q))
    elif command == 'empty':
        if q: print(0)
        else: print(1)
    elif command == 'front':
        if q: print(q[0])
        else: print(-1)
    elif command == 'back':
        if q: print(q[-1])
        else: print(-1)