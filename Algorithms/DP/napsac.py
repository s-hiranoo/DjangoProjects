# coding: utf-8

"""

問題 2:　ナップサック問題
n 個の品物があり、i 番目の品物のそれぞれ重さと価値が

 weight[i],value[i] となっている (i=0,1,...,n−1)。

これらの品物から重さの総和が W を超えないように選んだときの、価値の総和の最大値を求めよ。


【制約】
・1≤n≤100
・weight[i],value[i] は整数
・1≤weight[i],value[i]≤1000
・1≤W≤10000

"""

"""
dp[k][w]: k-1番目まで選んだときの価値の総和(wを超えない）
dp[0][w]: nothing chosen yet
"""

dp = [[0, 0]] * N*2

for i in range(N):
    if w >= weight[i+1]:
        dp[i+1][w] = max(dp[i][w-weight[i+1]]+value[i+1], dp[i][w])
    else:
        dp[i+1][w] = dp[i][w]

