'''
3524-find-x-value-of-array-i
'''

from typing import List


class Solution:
  def resultArray(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = [0]*k
    cnt = [0]*k

    for val in nums:
      cnt2 = [0]*k
      for r, c in enumerate(cnt):
        cnt2[(r*val) % k] += c
        res[(r*val) % k] += c

      # replace the subarray product remainder counter
      cnt = cnt2

      # val as the beginner elem of the new subarray
      cnt[val%k] += 1
      res[val%k] += 1

    return res
        