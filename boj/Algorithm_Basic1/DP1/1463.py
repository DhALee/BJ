import sys

n = int(sys.stdin.readline())
d = [-1 for _ in range(n+1)]

for i in range(1, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min([d[i], d[int(i//2)]+1])
    if i % 3 == 0:
        d[i] = min([d[i], d[int(i//3)]+1])

print(d[-1])
