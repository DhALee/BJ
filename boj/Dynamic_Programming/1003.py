T = int(input())

def fibo(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    if d[n] != (0, 0):
        return d[n]
    d[n] = (fibo(n - 1)[0] + fibo(n - 2)[0], fibo(n - 1)[1] + fibo(n - 2)[1])
    return d[n]

result = []
for _ in range(T):
    d = [(0, 0)] * 41
    d[0] = (1, 0)
    d[1] = (0, 1)
    n = int(input())
    fibo(n)
    result.append(d[n])

for (x, y) in result:
    print(x, y)