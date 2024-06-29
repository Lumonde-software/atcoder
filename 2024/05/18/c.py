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
a = []
b = []
m = {}

for i in range(n):
    aa, bb = NMI()
    a.append([aa, i])
    b.append([bb, i])
    m[i] = bb
a.sort(reverse=True)
b.sort(reverse=True)

ans = set([])
look = 0
visited = [False] * n
for i in range(n):
    x = a[i][0]
    if visited[a[i][1]]:
        continue
    y = m[a[i][1]]
    visited[a[i][1]] = True
    ans.add(a[i][1] + 1)
    while look < n:
        if y > b[look][0]:
            break
        visited[b[look][1]] = True
        look += 1

print(len(ans))
print(" ".join(map(str, sorted(list(ans)))))
