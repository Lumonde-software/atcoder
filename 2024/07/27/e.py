import random
import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import accumulate, combinations, permutations
from math import ceil, comb, factorial, floor, gcd, isqrt, lcm, log2, perm, sqrt
from string import ascii_lowercase, ascii_uppercase

inf = float("inf")
input = lambda: sys.stdin.readline().strip()
SI = lambda: input()
SLI = lambda: list(input().split())
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(map(int, input().split()))
N1MI = lambda: map(lambda x: int(x) - 1, input().split())
N1LI = lambda: list(map(lambda x: int(x) - 1, input().split()))
SEI = lambda m: [list(input().split()) for _ in range(m)]
NEI = lambda m: [list(map(int, input().split())) for _ in range(m)]
dir4 = ((-1, 0), (0, 1), (1, 0), (0, -1))
dir8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
mod = 998244353

n, x, y = NMI()
a = []
b = []

for _ in range(n):
    aa, bb = NMI()
    a.append(aa)
    b.append(bb)

# dp[i番目までの料理を考える][j+1個の料理を食べた][Aの合計がk] = Bの合計の最小値
dp = [[[inf] * (x + 1) for _ in range(i)] for i in range(n + 1)]
dp[1][0][0] = 0

for i in range(1, n):
    for j in range(i):
        for k in range(x + 1):
            if k + a[i] <= x and dp[i][j][k] + b[i] <= y:
                dp[i + 1][j + 1][k + a[i]] = min(dp[i + 1][j + 1][k + a[i]], dp[i][j][k] + b[i])
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])

ans = 0
for j in range(n):
    for k in range(x + 1):
        if dp[n][j][k] < inf:
            ans = j + 1
            break

print(min(ans, n))
