import sys

n = int(sys.stdin.readline())
d = [0, 1, 2]

for i in range(3, 1001):
    d.append(d[i - 2] + d[i - 1])

print(d[n] % 10007)