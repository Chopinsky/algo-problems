'''
3334-find-the-maximum-factor-score-of-array
'''

from math import lcm, gcd
from typing import List


class Solution:
  def maxScore(self, nums: List[int]) -> int:
    def lcm(a: int, b: int) -> int:
      return a * b // gcd(a, b)

    n = len(nums)
    
    # Prefix and suffix GCD
    prefix_gcd = [0] * (n + 1)
    suffix_gcd = [0] * (n + 1)
    
    for i in range(n):
      prefix_gcd[i + 1] = gcd(prefix_gcd[i], nums[i])
    
    for i in range(n - 1, -1, -1):
      suffix_gcd[i] = gcd(suffix_gcd[i + 1], nums[i])
    
    # Prefix and suffix LCM
    prefix_lcm = [1] * (n + 1)
    suffix_lcm = [1] * (n + 1)
    
    for i in range(n):
      prefix_lcm[i + 1] = lcm(prefix_lcm[i], nums[i])
    
    for i in range(n - 1, -1, -1):
      suffix_lcm[i] = lcm(suffix_lcm[i + 1], nums[i])
    
    # Case: no removal
    max_score = gcd(prefix_gcd[n], 0) * lcm(prefix_lcm[n], 1)
    
    # Case: remove one element
    for i in range(n):
      g = gcd(prefix_gcd[i], suffix_gcd[i + 1])
      l = lcm(prefix_lcm[i], suffix_lcm[i + 1])
      max_score = max(max_score, g * l)
    
    return max_score
  
  def maxScore(self, nums: List[int]) -> int:
    def get_score(arr: List) -> int:
      l = arr[0]
      g = arr[0]

      for val in arr[1:]:
        l = lcm(l, val)
        g = gcd(g, val)

      return l*g

    score = get_score(nums)
    n = len(nums)
    if n == 1:
      return score

    for i in range(n):
      score = max(
        score,
        get_score([nums[j] for j in range(n) if j != i])
      )

    return score
