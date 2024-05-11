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
m = 998244353
mod = 10**9 + 7
RANDOM = random.randint(1217, 2000)

n = NI()
a = NLI()

a.sort()

lens = [[] for _ in range(11)]
for i in range(n):
    lens[len(str(a[i]))].append(a[i])

l = [len(lens[i]) for i in range(11)]

lu = [l[i] for i in range(11)]
luu = [l[i] for i in range(11)]
for i in range(1, 11):
    tmp = 0
    for j in range(l[i]):
        if lens[i][j] >= int(str(m)[:i]):
            tmp += 1
            break
    lu[i] = l[i] - tmp
    while j < l[i] and lens[i][j] == int(str(m)[:i]):
        j += 1
        tmp += 1
    luu[i] = l[i] - tmp


ld = [l[i] for i in range(11)]
ldu = [l[i] for i in range(11)]
for i in range(1, 11):
    tmp = 0
    for j in range(l[i]):
        if lens[i][j] < int(str(m)[-i:]):
            tmp += 1
            break
    ld[i] = l[i] - tmp
    while j < l[i] and lens[i][j] == int(str(m)[-i:]):
        j += 1
        tmp += 1
    ldu[i] = l[i] - tmp

cnt = 0
for i in range(1, 11):
    for j in range(i + 1, 11):
        if i + j > 9:
            cnt += l[i] * l[j]
        elif i + j == 9:
            if lu[i] == l[i]:
                if ld[j] == l[j]:
                    continue
                elif ldu[i] == l[j]:
                    cnt += lu[i] * (ldu[j] - ld[j])
                    continue
                cnt += lu[i] * (ldu[j] - ld[j])
                cnt += l[i] * ldu[j]
            elif ld[j] == l[j]:
                if luu[i] == l[i]:
                    cnt += (luu[i] - lu[i]) * ld[j]
                    continue
                cnt += (luu[i] - lu[i]) * ld[j]
                cnt += luu[i] * l[j]
            else:
                cnt += (luu[i] - lu[i]) * ld[j]
                cnt += lu[i] * (ldu[j] - ld[j])
                cnt += luu[i] * l[j]
                cnt += l[i] * ldu[j]

s = 0
ls = sum([l[i] * 10**i for i in range(11)])
for i in range(1, 11):
    lls = ls - 10**i
    for j in range(l[i]):
        s += lens[i][j] * lls
        s += lens[i][j] * (n - 1)
        if s >= m and cnt > 0:
            s -= m
            cnt -= 1

s -= m * cnt

print(s)
