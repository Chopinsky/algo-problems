'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


from typing import List
from collections import Counter


class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    c = Counter(nums)
    n = len(nums)
    base = sorted(c)
    comb, ans = [], []
    
    def perm():
      if len(comb) == n:
        ans.append(list(comb))
        return
      
      for val in base:
        if not c[val]:
          continue
          
        comb.append(val)
        c[val] -= 1
        
        perm()
        
        comb.pop()
        c[val] += 1
        
    perm()
    return ans
    