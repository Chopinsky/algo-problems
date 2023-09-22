'''
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
'''

from typing import List
import math

class Solution:
  def minOperations(self, nums: List[int], x: int) -> int:
    n = len(nums)
    total = sum(nums)
    
    if total <= x:
      return n if total == x else -1
    
    target = total - x
    if nums[0] == target:
      return n-1
    
    l, r = 0, 0
    sums = 0
    ops = math.inf
    
    while l < n:
      while r < n and sums < target:
        sums += nums[r]
        r += 1
      
      if sums == target:
        # print(sums, (l, r))
        ops = min(ops, n-(r-l))
        
      sums -= nums[l]
      l += 1
    
    return -1 if ops == math.inf else ops
        

  def minOperations(self, nums: List[int], x: int) -> int:
    prefix = {0: 0}
    n = len(nums)
    ops = math.inf
    sums = 0
    
    for i in range(n):
      sums += nums[i]
      if sums > x:
        break
        
      if sums == x:
        ops = min(ops, i+1)
        # print('prefix:', i)
        
      if sums not in prefix:
        prefix[sums] = i + 1
        
    sums = 0
    for i in range(n-1, -1, -1):
      sums += nums[i]
      if sums > x:
        break
        
      if sums == x:
        ops = min(ops, n-i)
        
      if x-sums in prefix:
        ln = prefix[x-sums]
        if ln-1 >= i:
          break
        
        ops = min(ops, n-i+prefix[x-sums])
        # print('mix:', i, n-i, prefix[x-sums])
        
    return -1 if ops == math.inf else ops


  def minOperations0(self, nums: List[int], x: int) -> int:
    dic = {}
    prefix = 0
    long = -1
    y = sum(nums) - x
    n = len(nums)
    
    for i, val in enumerate(nums):
      prefix += val
      if prefix == x:
        long = max(long, n-i-1)
      
      if prefix == y:
        long = max(long, i+1)
      
      if prefix-y in dic:
        long = max(long, i-dic[prefix-y])
        # print(prefix, i, dic[prefix-y])
        
      if prefix not in dic:
        dic[prefix] = i
        
    # print(long)
    return -1 if long < 0 else n-long
  