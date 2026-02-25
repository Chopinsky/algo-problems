'''
3314-construct-the-minimum-bitwise-array-i
'''

from typing import List


vals = dict[int, int]()

for val in range(1001):
  t = val | (val+1)
  if t not in vals:
    vals[t] = val


class Solution:
  def minBitwiseArray(self, nums: List[int]) -> List[int]:
    # print('init:', vals)
    return [-1 if val not in vals else vals[val] for val in nums]
        