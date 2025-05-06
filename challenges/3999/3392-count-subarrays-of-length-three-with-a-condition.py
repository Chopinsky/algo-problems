'''
3392-count-subarrays-of-length-three-with-a-condition
'''

from typing import List


class Solution:
  def countSubarrays(self, nums: List[int]) -> int:
    cnt = 0
    n = len(nums)
    curr = nums[0]+nums[1]

    for i in range(n-2):
      curr += nums[i+2]
      if i > 0:
        curr -= nums[i-1]
      
      # print('iter:', i, curr)
      if nums[i+1] == 2*(curr-nums[i+1]):
        cnt += 1

    return cnt
        