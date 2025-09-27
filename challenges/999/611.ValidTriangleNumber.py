'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:

Input: nums = [4,2,3,4]
Output: 4

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
'''


from typing import List
from bisect import bisect_right


class Solution:
  def triangleNumber(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
      return 0

    nums.sort()
    count = 0
    k = 0

    for i in range(n-2):
      v0 = nums[i]
      k = 0

      for j in range(i+1, n-1):
        v1 = nums[j]

        while k < n and nums[k] < v0+v1:
          k += 1

        # print('iter:', (i, j), k, k-j-1)
        if k > j:
          count += k-j-1

    return count

  def triangleNumber(self, nums: List[int]) -> int:      
    n = sorted(nums)
    ln = len(n)
    count = 0
    # print(n)
    
    for i in range(ln-2):
      for j in range(i+1, ln-1):
        tgt = n[i] + n[j] - 1
        idx = bisect_right(n, tgt)-1
        
        if idx > j and idx < ln:
          # print(n[i], n[j], n[idx], tgt)
          count += idx-j
          
    return count
  