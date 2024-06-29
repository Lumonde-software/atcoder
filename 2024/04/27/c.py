import sys
import random
from math import gcd, lcm, sqrt, isqrt, perm, comb, factorial, log2, ceil, floor
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from copy import deepcopy
from bisect import bisect_left, bisect_right
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
mod99 = 998244353
mod = 10**9 + 7
RANDOM = random.randint(1217, 2000)

n = NI()
a = NLI()

m = {}

for i in range(n):
    if i == 0:
        m[i] = [a[i], None, i + 1]
    elif i == n - 1:
        m[i] = [a[i], i - 1, None]
    else:
        m[i] = [a[i], i - 1, i + 1]

cnt = 0
for i in range(1, n):
    while True:
        if (m[i][1] is not None) and m[i][0] == m[m[i][1]][0]:
            m[i][0] += 1
            m[i][1] = m[m[i][1]][1]
            cnt += 1
        else:
            break

print(n - cnt)
