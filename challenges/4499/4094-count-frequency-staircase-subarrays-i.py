'''
4094-count-frequency-staircase-subarrays-i
'''

from collections import defaultdict


class Solution:
  def countStaircase(self, nums: list[int]) -> int:
    n = len(nums)
    cnt = 0

    def count(i: int) -> int:
      c = 0
      e = {}
      counter = defaultdict(int)
      less = set()

      for j in range(i, n):
        val = nums[j]
        if val not in e:
          e[val] = len(e)+1
          less.add(val)

        counter[val] += 1
        if counter[val] > e[val]:
          break

        if counter[val] == e[val]:
          less.discard(val)

        if not less:
          c += 1

      return c

    for i in range(n):
      cnt += count(i)

    return cnt
