for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for j in range(1, m):
        for k in range(n):
            if k == 0:
                dp[k][j] = dp[k][j] + max(dp[k][j - 1], dp[k + 1][j - 1])
            elif k == n - 1:
                dp[k][j] = dp[k][j] + max(dp[k][j - 1], dp[k - 1][j - 1])
            else:
                dp[k][j] = dp[k][j] + max(dp[k][j - 1], dp[k - 1][j - 1], dp[k + 1][j - 1])
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
    # print(dp[n - 1][m - 1])
