'''
3510-minimum-pair-removal-to-sort-array-ii
'''

from typing import List


class Solution:
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
      val, i = s.pop(0)
      j = r[i]
      h, k = l[i], r[j]
      
      remove(h)
      remove(i)
      remove(j)

      nums[i] += nums[j]
      r[i] = k
      if k < n:
        l[k] = i

      add(h)
      add(i)

    return ans
        