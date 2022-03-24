'''
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
 

Constraints:

3 <= nums.length <= 10^5
0 <= nums[i] <= 10^4
'''


from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def waysToSplit(self, nums: List[int]) -> int:
    if len(nums) == 3:
      return 1 if nums[0] <= nums[1] <= nums[2] else 0
    
    prefix = nums
    n = len(nums)
    count = 0
    mod = 10 ** 9 + 7
    
    for i in range(1, n):
      prefix[i] += prefix[i-1]
      
    # print('prefix:', prefix, n)
    
    for i in range(n-2):
      tail_sums = prefix[-1] - prefix[i]
      if tail_sums < 2 * prefix[i]:
        break
      
      j = max(i+1, bisect_left(prefix, 2 * prefix[i]))
      # print('j', i, j, prefix[j]-prefix[i], prefix[-1]-prefix[j])
      if j >= n-1 or (prefix[j]-prefix[i]) > (prefix[-1]-prefix[j]):
        continue
      
      k = min(n-2, bisect_right(prefix, prefix[i] + (tail_sums//2)) - 1)
      # print('k', i, k, prefix[k]-prefix[i], prefix[-1]-prefix[k])
      if k < j or (prefix[k]-prefix[i]) > (prefix[-1]-prefix[k]):
        break
        
      count = (count + (k-j+1)) % mod
      # print(i, tail_sums, (j, prefix[j]), (k, prefix[k]))
    
    return count
      