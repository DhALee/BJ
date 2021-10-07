import sys

T = int(sys.stdin.readline())
d = [0, 1, 2, 4]

for i in range(4, 11):
    d.append(d[i - 3] + d[i - 2] + d[i - 1])
for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n])
