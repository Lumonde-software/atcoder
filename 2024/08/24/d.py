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

n, k = NMI()
ab = [[] for _ in range(n+1)]
for _ in range(n-1):
    aa, bb = NMI()
    ab[aa].append(bb)
    ab[bb].append(aa)
v = NLI()
set_v = set(v)

arrived = set([])
arriving = set([v[0]])
def dfs(p, w):
    w.append(p)
    if p in set_v:
        for ww in w:
            arrived.add(ww) 
        w = []

    for nxt in ab[p]:
        if nxt not in arriving:
            arriving.add(nxt)
            dfs(nxt, w.copy())

    del w
    return   

dfs(v[0], [])

print(len(arrived))