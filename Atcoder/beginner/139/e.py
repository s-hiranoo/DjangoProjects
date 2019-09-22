# coding: utf-8
import numpy as np

N = int(input())
x = np.zeros(N)
y = np.zeros(N)
r = np.zeros(N)

for i in range(N):
    x[i], y[i] = map(int, input().split())
    r[i] = np.arctan2(y[i], x[i])

    print('\nx, y, r: ', x[i], ' ', y[i], ' ', r[i])

sort_index = np.argsort(r)
x = x[sort_index]
y = y[sort_index]
r = r[sort_index]

point = [x[0], y[0]]
for i in range(N):
    if i==0:
        continue

    dot = point[0]*x[i] + point[1]*y[i]
    if dot > 0:
        point[0] += x[i]
        point[1] += y[i]

print(np.sqrt(point[0]**2 + point[1]**2))





