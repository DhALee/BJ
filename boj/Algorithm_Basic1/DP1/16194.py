import sys

n = int(sys.stdin.readline())
price = [0] + list(map(int, sys.stdin.readline().split()))
d = [0] + [10000 for i in range(1, len(price))]

for i in range(1, len(d)):
    for j in range(1, i + 1):
        if d[i] > d[i - j] + price[j]:
            d[i] = d[i - j] + price[j]

print(d[n])
