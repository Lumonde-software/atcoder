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

n, t = NMI()
s = SI()
x = NLI()

ones = [x[i] for i in range(n) if s[i] == "1"]
zeros = [x[i] for i in range(n) if s[i] == "0"]

if len(zeros) == 0:
    print(0)
    exit()

left = 0
right = 0
flag_left = True
ans = 0
for i in range(len(ones)):
    flag_right = True
    target = ones[i]
    while True:
        if zeros[left] < target:
            if left == len(zeros) - 1:
                flag_left = False
                break
            left += 1
        else:
            break
    while True:
        if zeros[right] <= target + 2 * t:
            if right == len(zeros) - 1:
                break
            if zeros[right + 1] <= target + 2 * t:
                right += 1
            else:
                break
        else:
            flag_right = False
            break
    if not flag_left:
        break
    if not flag_right:
        continue
    ans += right - left + 1

print(ans)
