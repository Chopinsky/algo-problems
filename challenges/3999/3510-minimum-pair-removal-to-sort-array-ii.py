'''
3510-minimum-pair-removal-to-sort-array-ii
'''

from typing import List
import math
from heapq import heappush, heappop

from sortedcontainers import SortedList


class Solution:
  def minimumPairRemoval(self, nums: List[int]) -> int:
    n = len(nums)
    prev = [i-1 for i in range(n+1)]
    nxt = [i+1 if i < n-1 else -1 for i in range(n)]
    nxt.append(0)

    q = []
    bad = 0

    for i in range(1, n):
      if nums[i-1] > nums[i]:
        bad += 1

      heappush(q, (nums[i-1]+nums[i], i))

    ans = 0
    while bad > 0:
      # print(ans, bad, nums, q)
      s, r = heappop(q)
      l = prev[r]

      # illegal or stale state
      if l == -1 or nums[l] + nums[r] != s:
        continue

      nxt[l] = nxt[r]
      prev[nxt[r]] = l

      if nums[l] > nums[r]:
        bad -= 1

      ll = prev[l]
      if ll != -1:
        bad += (nums[ll] > s) - (nums[ll] > nums[l])
        heappush(q, (nums[ll]+s, l))

      rr = nxt[r]
      if rr != -1:
        bad += (s > nums[rr]) - (nums[r] > nums[rr])
        heappush(q, (nums[rr]+s, rr))

      nums[l] = s
      nums[r] = math.inf
      ans += 1

    return ans

  def minimumPairRemoval(self, nums: List[int]) -> int:
    n = len(nums)
    l = list(range(-1, n-1))
    r = list(range(1, n+1))
    inversions = sum(nums[i] > nums[i+1] for i in range(n-1))
    s = SortedList([nums[i]+nums[i+1], i] for i in range(n-1))

    def add(i: int):
      nonlocal inversions

      j = r[i]
      if 0<= i < j < n:
        s.add([nums[i]+nums[j], i])
        inversions += nums[i] > nums[j]

    def remove(i: int):
      nonlocal inversions

      j = r[i]
      if 0 <= i < j < n:
        s.discard([(nums[i]+nums[j]), i])
        inversions -= nums[i] > nums[j]

    ans = 0
    while inversions > 0:
      ans += 1
      _, i = s.pop(0)
      j = r[i]
      ll, rr = l[i], r[j]
      
      remove(ll)
      remove(i)
      remove(j)

      nums[i] += nums[j]
      r[i] = rr
      if rr < n:
        l[rr] = i

      add(ll)
      add(i)

    return ans
        