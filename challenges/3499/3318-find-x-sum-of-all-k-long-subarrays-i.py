'''
3318-find-x-sum-of-all-k-long-subarrays-i
'''

from collections import Counter
from typing import List


class Solution:
  def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    counter = Counter(nums[:k])
    n = len(nums)

    def calc(c) -> int:
      cand = sorted(c.items(), key=lambda x: (x[1], x[0]))
      res = 0
      rem = x

      while cand and rem > 0:
        val, cnt = cand.pop()
        res += val*cnt
        rem -= 1

      return res

    result = [calc(counter)]
    # print('done:', counter)

    for i in range(k, n):
      val = nums[i]
      prev = nums[i-k]
      counter[val] += 1
      counter[prev] -= 1
      result.append(calc(counter))

    return result
        