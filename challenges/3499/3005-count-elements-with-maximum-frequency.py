'''
3005-count-elements-with-maximum-frequency
'''

from typing import List
from collections import Counter


class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    c = Counter(nums)
    max_cnt = max(c.values())
    cand = [val for val in c if c[val] == max_cnt]
    return len(cand)*max_cnt
