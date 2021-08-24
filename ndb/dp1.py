n = int(input())
house = list(map(int, input().split()))
d = [0] * 100

d[0] = house[0]
d[1] = max(house[0], house[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + house[i])

print(d[n - 1])

