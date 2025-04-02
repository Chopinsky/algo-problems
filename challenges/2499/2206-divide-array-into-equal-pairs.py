'''
2206-divide-array-into-equal-pairs
'''

from collections import Counter
from typing import List


class Solution:
  def divideArray(self, nums: List[int]) -> bool:
    c = Counter(nums)
    return all(cnt%2 == 0 for cnt in c.values())    
    