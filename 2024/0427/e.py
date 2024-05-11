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
odd = []
even = []
for _ in range(n):
    x, y = NMI()
    if (x + y) % 2:
        odd.append(max(x, y))
    else:
        even.append(max(x, y))

ans = 0
odd_sum = sum(odd)
even_sum = sum(even)

odd_len = len(odd)
even_len = len(even)

odd.sort()
even.sort()

print(odd, even)

for i in range(len(odd) - 1):
    odd_sum -= odd[i]
    ans += odd_sum - odd[i] * (odd_len - i - 1)
    print(i, odd_sum - odd[i] * (odd_len - i - 1))

for i in range(len(even) - 1):
    even_sum -= even[i]
    ans += even_sum - even[i] * (even_len - i - 1)
    print(i, even_sum - even[i] * (even_len - i - 1))

print(ans)
