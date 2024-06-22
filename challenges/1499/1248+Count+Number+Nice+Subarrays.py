'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''

from typing import List

class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    odd_pos = []
    total = 0
    
    for i, val in enumerate(nums):
      if val%2 == 1:
        odd_pos.append(i)
        
      if len(odd_pos) >= k:
        ldx = len(odd_pos)-k
        left_count = odd_pos[ldx] - (-1 if ldx == 0 else odd_pos[ldx-1])
        total += left_count
        # print('iter:', (i, val), left_count)
        
    return total
  
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    n = len(nums)
    odd = []
    
    for i in range(n):
      if nums[i] % 2 == 1:
        odd.append(i)
    
    # print(odd)
    if len(odd) < k:
      return 0
    
    count = 0
    ln = len(odd)
    
    for i in range(k-1, ln):
      r = (odd[i+1] if i != ln-1 else n) - odd[i]
      l = odd[i-k+1]+1 if i == k-1 else (odd[i-k+1] - odd[i-k])
      
      # print(i, l, r)
      count += r * l
    
    return count
    