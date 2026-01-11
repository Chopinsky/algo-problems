'''
1018-binary-prefix-divisible-by-5
'''

from typing import List


class Solution:
  def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    val = 0
    ans = []

    for v in nums:
      val = (val << 1) | v
      ans.append(val%5 == 0)

    return ans
        