'''
3233. Find the Count of Numbers Which Are Not Special
'''

from math import isqrt
from bisect import bisect_left, bisect_right


class Solution:
  def nonSpecialCount(self, l: int, r: int) -> int:
    total = r-l+1
    top = 2+isqrt(r)
    nums = []
    
    siv = [i for i in range(top)]
    for v0 in range(2, top):
      if siv[v0] < v0:
        continue
        
      nums.append(v0*v0)
      for v1 in range(v0*v0, top, v0):
        siv[v1] = v0
        
    i = bisect_left(nums, l)
    j = bisect_right(nums, r)-1
    cnt = j-i+1
    
    # print('init:', siv, nums)
    # print('found:', cnt, (i, j))
    
    return total - cnt
    