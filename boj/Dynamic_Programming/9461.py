def triangle(N):
    tri = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(11, 101):
        tri.append(tri[i-2] + tri[i-3])
    return tri[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(triangle(N))