# coding: utf-8

N = int(input())
H = list(map(int, input().split()))

dp = [0] * (N+1)
# dp[i+1]: H[i]に降りたときの最大移動回数

for n in range(N):
    i = N - n
    if i == N:
        continue

    if H[i-1] >= H[i]:
        dp[i-1] = dp[i] + 1
    else:
        dp[i-1] = 0

result = max(dp)

print(result)

