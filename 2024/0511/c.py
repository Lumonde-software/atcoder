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
m = 10**8

left = 0
right = n - 1

cnt = 0

a.sort()

while left < right:
    if a[left] + a[right] >= m:
        right -= 1
        if a[left] == a[right]:
            if a[left] * 2 < m:
                cnt += (n - 1 - right) * (right - left + 1)
                left = right + 1
            break
    else:
        left += 1
        cnt += n - 1 - right


cnt += (n - 1 - left) * (n - 1 - left + 1) // 2

s = 0
for aa in a:
    s += aa * (n - 1)
    if s >= m and cnt > 0:
        s -= m
        cnt -= 1

s -= m * cnt

print(s)
