'''
You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Example 1:

Input: nums = [4,6,15,35]
Output: 4
Example 2:

Input: nums = [20,50,9,63]
Output: 2
Example 3:

Input: nums = [2,3,6,7,4,12,21,39]
Output: 8

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^5
All the values of nums are unique.
'''


from functools import lru_cache
from typing import List
from collections import defaultdict


class Solution:
  @lru_cache(None)
  def get_sive(self, n: int) -> List[int]:
    s = [i for i in range(n+1)]
    for i in range(2, n+1):
      if s[i] < i:
        continue
        
      for j in range(i*i, n+1, i):
        s[j] = i
        
    return s
    
  def largestComponentSize(self, nums: List[int]) -> int:
    m, n = max(nums), len(nums)
    arr = [i for i in range(m+1)]
    count = defaultdict(int)
    sive = self.get_sive(m)
    
    def find(i: int) -> int:
      while arr[i] != i:
        i = arr[i]
        
      return i
    
    def union(i: int, j: int):
      idx, jdx = find(i), find(j)
      
      if idx <= jdx:
        arr[jdx] = idx
      else:
        arr[idx] = jdx
        
    for n in nums:
      val = n
      while val > 1:
        factor = sive[val]
        if factor != n and factor != 1:
          union(factor, n)
          
        val //= factor
        # print(n, factor)
        
      # print('group', n, find(n))
      
    for n in nums:
      count[find(n)] += 1
      
    # print(count)
    return max(count.values())
      