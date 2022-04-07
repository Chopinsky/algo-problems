'''
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^5
'''

from typing import List


class Solution:
  '''
  check if we can add op to the smaller numbers in the window 
  to match the `n_win * nums[r]`
  '''
  def maxFrequency(self, nums: List[int], k: int) -> int:
    nums.sort()
    sums = 0
    n = len(nums)
    
    # init the sliding window
    l, r = 0, 0
    while r < n and nums[l] == nums[r]:
      sums += nums[r]
      r += 1
    
    max_len = r - l
    # print(l, r)
    
    while r < n:
      # now include nums[r] into the window
      # and move the left boundary
      while l < r and (r-l)*nums[r] > sums+k:
        sums -= nums[l]
        l += 1
        
      max_len = max(max_len, r-l+1)
      sums += nums[r]
      # print('iter', l, r)
      r += 1
    
    return max_len
    