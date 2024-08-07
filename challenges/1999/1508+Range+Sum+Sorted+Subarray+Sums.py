'''
1508. Range Sum of Sorted Subarray Sums

You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 
Example 2:

Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
Example 3:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50

Constraints:

n == nums.length
1 <= nums.length <= 1000
1 <= nums[i] <= 100
1 <= left <= right <= n * (n + 1) / 2
'''

from typing import List

class Solution:
  def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    mod = 10**9 + 7
    s = []
    prefix = [val for val in nums]
    n = len(nums)
    
    for i in range(1, n):
      prefix[i] += prefix[i-1]
    
    for i in range(n):
      for j in range(i+1):
        s0 = prefix[i] - (prefix[j-1] if j > 0 else 0)
        s.append(s0)
        
    s.sort()
    rs = 0
    # print(s)
    
    for i in range(left-1, right):
      rs = (rs + s[i]) % mod
      
    return rs
  
  def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    mod = 10**9 + 7
    arr = []

    for i in range(n):
      curr = 0
      for j in range(i, n):
        curr += nums[j]
        arr.append(curr)
        
    arr.sort()
    res = 0
    # print(arr)
    
    for val in arr[left-1:right]:
      res = (res + val) % mod
      
    return res
        