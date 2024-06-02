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
mod = 998244353

n, m = NMI()
n_bit_list = []
m_bit_list = []
for j in range(60):
    n_bit = (n >> j) & 1
    m_bit = (m >> j) & 1
    n_bit_list.append(n_bit)
    m_bit_list.append(m_bit)

nm_bit_list = [n_bit_list[i] & m_bit_list[i] for i in range(60)]

ans = 0
for i in reversed(range(60)):
    if n_bit_list[i]:
        if i > 0:
            ans += (2 ** (i - 1) % mod) * sum(m_bit_list[:i])
            ans %= mod

        if i + 1 < 60:
            ans += (2**i % mod) * sum(nm_bit_list[i + 1 :])
            ans %= mod

        if m_bit_list[i]:
            ans += 1
            ans %= mod

print(ans)
