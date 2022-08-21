'''
2386. Find the K-Sum of an Array

You are given an integer array nums and a positive integer k. You can choose any subsequence of the array and sum all of its elements together.

We define the K-Sum of the array as the kth largest subsequence sum that can be obtained (not necessarily distinct).

Return the K-Sum of the array.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Note that the empty subsequence is considered to have a sum of 0.

Example 1:

Input: nums = [2,4,-2], k = 5
Output: 2
Explanation: All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
- 6, 4, 4, 2, 2, 0, 0, -2.
The 5-Sum of the array is 2.

Example 2:

Input: nums = [1,-2,3,4,-10,12], k = 16
Output: 10
Explanation: The 16-Sum of the array is 10.

Constraints:

n == nums.length
1 <= n <= 10^5
-10^9 <= nums[i] <= 10^9
1 <= k <= min(2000, 2^n)
'''

from typing import List
from heapq import heappop, heappush


class Solution:
  '''
  a rather difficult problem: the idea is to build the largest subseq sums sequencially; 
  we begin with the biggest subseq sum, which is the sum of all non-negative numbers; then
  the next largest sum is `max_sum - min(abs(nums))`, since substracting `min(abs(positive_number))`
  is the same as adding `max(abs(negative_number))` from the last big sum, we can create 
  a candidate list using `sorted(abs(nums))`; then for each last big sum at count-i, we can 
  derive 2 possible candidates for the next big sum: `src - nxt_cand`, or `latest_big_sum - nxt_cand`,
  this will compound the combination of removing a positive number from the subseq, or adding a 
  negative number to the subseq; we just use priority queue to take the biggest subseq sum from
  a pile of possible big sums for the next largest subseq sum, then repeat the process to get
  the k-th largest subseq sum for the array.
  '''
  def kSum(self, nums: List[int], k: int) -> int:
    last = 0
    n = len(nums)
    
    for i in range(n):
      if nums[i] > 0:
        last += nums[i]
        
      nums[i] = abs(nums[i])
      
    nums.sort()
    stack = [(-last+nums[0], last, 0)]
    cnt = 1
    
    while cnt < k:
      top, src, idx = heappop(stack)
      last = -top
      cnt += 1
      
      if idx+1 < n:
        idx += 1
        heappush(stack, (-src+nums[idx], src, idx))
        heappush(stack, (-last+nums[idx], last, idx))
      
      # print(cnt, last, stack)
      
    return last
        