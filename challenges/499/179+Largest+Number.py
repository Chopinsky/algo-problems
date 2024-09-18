'''
179. Largest Number
'''

from functools import cmp_to_key
from typing import List

class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    cand = sorted([str(val) for val in nums], key=cmp_to_key(lambda x, y: -1 if x+y > y+x else 1))
    if cand[0] == '0':
      return '0'
    
    return ''.join(cand)
        