'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

1 <= nums.length <= 2500
-10 ** 4 <= nums[i] <= 10 ** 4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''


from typing import List
from bisect import bisect_left


class Solution:
  '''
  idea is to maintain the longest subarr we can obtain from the array; we rebuild 
  the array if a number that can be inserted into the middle of the array, where a 
  new sequence can start building up; then we keep track of the longest such subsequence
  we have obtained so far.
  '''
  def lengthOfLIS(self, nums: List[int]) -> int:
    arr = []
    ans = 0
    
    for n in nums:
      if len(arr) == 0 or n > arr[-1]:
        arr.append(n)

        if len(arr) > ans:
          ans = len(arr)

        continue
        
      idx = bisect_left(arr, n)
      arr[idx] = n

      '''
      the steps below can be omitted, which will make the algo clearer but less
      efficient by a hair:
      arr = arr[:idx+1]
      '''
    
    # print(arr)
    
    return ans