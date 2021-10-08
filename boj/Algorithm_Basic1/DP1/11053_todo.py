import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
d = [0 for _ in range(n)]

for i in range(n):
    count = 1
    maximum = seq[i]
    for j in range(i + 1, n):
        if maximum < seq[j]:
            maximum = seq[j]
            count += 1
    d[i] = count

print(max(d))
