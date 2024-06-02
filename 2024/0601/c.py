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

n, m, k = NMI()
c = []
a = []
r = []
for _ in range(m):
    cc, *aa, rr = input().split()
    c.append(int(cc))
    a.append(list(map(int, aa)))
    r.append(rr)

cnt = 0
for i in range(2**n):
    bit_list = []
    for j in range(n):
        bit = (i >> j) & 1
        bit_list.append(bit)

    flag = True
    for j in range(m):
        cc = c[j]
        aa = a[j]
        rr = r[j]

        cnt_correct_keys = 0
        for l in range(cc):
            if bit_list[aa[l] - 1]:
                cnt_correct_keys += 1

        if rr == "o" and cnt_correct_keys < k:
            flag = False
            break
        elif rr == "x" and cnt_correct_keys >= k:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)
