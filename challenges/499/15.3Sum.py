'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

Constraints:

0 <= nums.length <= 3000
-10 ** 5 <= nums[i] <= 10 ** 5
'''


from typing import List


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    c = {}
    for n in nums:
      if n in c:
        c[n] += 1
      else:
        c[n] = 1
    
    un = sorted(set(nums))
    seen = set()
    ans = []
    
    for n0 in un:
      for n1 in un:
        # print("pre", n0, n1)
        # n0, n1 = min(n0, n1), max(n0, n1)
        
        if (n0, n1) in seen:
          continue
          
        n2 = -n0-n1
        if n2 not in c:
          continue
        
        # print("match", n0, n1, n2)
        c[n0] -= 1
        c[n1] -= 1
        c[n2] -= 1
        
        if c[n0] >= 0 and c[n1] >= 0 and c[n2] >= 0:
          arr = sorted([n0, n1, n2])
          if (arr[0], arr[1]) not in seen:
            seen.add((arr[0], arr[1]))
            ans.append(arr)
            # print(arr)
          
        c[n0] += 1
        c[n1] += 1
        c[n2] += 1
        
    # print(seen, c)
    
    return ans
    