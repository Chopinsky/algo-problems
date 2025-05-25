'''
3024-type-of-triangle
'''

from typing import List


class Solution:
  def triangleType(self, nums: List[int]) -> str:
    nums.sort()
    a, b, c = nums
    if a+b <= c:
      return "none"

    if a == b == c:
      return "equilateral"

    if a == b or b == c:
      return "isosceles"

    return "scalene"
        