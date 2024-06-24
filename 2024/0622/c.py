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

sx, sy = NMI()
tx, ty = NMI()

dx = abs(tx - sx)
dy = abs(ty - sy)

cx = dx//2
if dx % 2 == 1 and ((sx + sy) % 2 == 0 and tx < sx or (sx + sy) % 2 == 1 and tx > sx):
    cx += 1

if cx < dy:
    print(max(cx, dy))
else:
    ddx = abs(dx - dy)
    if ((sx + sy) % 2 == 0 and tx > sx) or ((sx + sy) % 2 == 1 and tx < sx):
        ddx -= 1
    ssx = tx + ddx * (-1 if tx > sx else 1)
    ccx = ddx//2
    if ddx % 2 == 1 and (ssx % 2 == 0 and tx < ssx or ssx % 2 == 1 and tx > ssx):
        ccx += 1
    
    print(ccx + dy)