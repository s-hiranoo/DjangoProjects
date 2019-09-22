# coding: utf-8

"""

問題 3:　部分和問題　
n 個の正の整数 a[0],a[1],…,a[n−1] と正の整数 A が与えられる。
これらの整数から何個かの整数を選んで総和が A になるようにすることが可能か判定せよ。
可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。

【制約】
・1≤n≤100
・1≤a[i]≤1000
・1≤A≤10000

"""

"""
dp[i][j]: true if j can be created by summation from a[0], ..., a[i-1] 

"""

dp

for i in range(N):
    for j in range(A):
        dp[i+1][j] = dp[i][j]
        if (not dp[i][j]) and j >= a[i]:
            dp[i+1][j] = dp[i][j-a[i]]
