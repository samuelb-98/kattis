from math import factorial
from sys import stdin


def solve(n):
    dp = [[0 for i in range(8)]for i in range(n+1)]
    dp[0][7] = 1
    for i in range(1,n+1):
        dp[i][0] = dp[i-1][7]
        dp[i][1] = dp[i-1][6]
        dp[i][2] = dp[i-1][5]
        dp[i][3] = dp[i-1][7] + dp[i-1][4]
        dp[i][4] = dp[i-1][3]
        dp[i][5] = dp[i-1][2]
        dp[i][6] = dp[i-1][7] + dp[i-1][1]
        dp[i][7] = dp[i-1][6] + dp[i-1][3] + dp[i-1][0]
    return(dp[n][7])


for line in stdin:
    n = int(line)
    if n == -1:
        break
    
    print(solve(n))