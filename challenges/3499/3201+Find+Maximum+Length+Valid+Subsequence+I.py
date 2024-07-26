'''
3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].

Constraints:

2 <= nums.length <= 2 * 10^5
1 <= nums[i] <= 10^7
'''

from typing import List

class Solution:
  def maximumLength(self, nums: List[int]) -> int:
    arr = [val%2 for val in nums]
    long = max(arr.count(0), arr.count(1))
    prev, ln = arr[0], 1
    # print(arr, long)
    
    for val in arr[1:]:
      # print(val, prev)
      if val == 1-prev:
        ln += 1
        prev = val
        
    return max(ln, long)
  