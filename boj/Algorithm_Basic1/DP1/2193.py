import sys

n = int(sys.stdin.readline())
d = [[0] * 2 for _ in range(91)]

d[1] = [0, 1]
d[2] = [1, 0]
d[3] = [1, 1]

for i in range(4, 91):
    d[i][0], d[i][1] = d[i - 1][0] + d[i - 1][1], d[i - 1][0]

print(sum(d[n]))