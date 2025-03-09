'''
3480-maximize-subarrays-after-removing-one-conflicting-pair
'''

from typing import List


class Solution:
  def maxSubarrays(self, n: int, pairs: List[List[int]]) -> int:
    right = [[] for _ in range(n + 1)]
    for a, b in pairs:
      l = min(a, b)
      r = max(a, b)
      right[r].append(l)
    
    ans = 0
    left = [0, 0]
    imp = [0] * (n+1)
    for r in range(1, n+1):
      for l in right[r]:
        left = max(left, [l, left[0]], [left[0], l])
      
      # all subarrays of [x, r] where x > left[0] is valid
      ans += r - left[0]

      # if remove left[0], we can unlock subarrays of [x, r] where x > left[1]
      imp[left[0]] += left[0] - left[1]
    
    return ans + max(imp)
