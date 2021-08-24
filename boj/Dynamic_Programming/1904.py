def binary(N):
    bin = [0, 1, 2, 3, 5]
    for i in range(5, 1000001):
        bin.append((bin[i-1] + bin[i-2])%15746)

    return bin[N]

T = int(input())
print(binary(T))