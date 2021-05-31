'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Constraints:

1 <= nums.length <= 10 ** 4
0 <= nums[i] <= 10 ** 9
'''

from collections import defaultdict
from typing import List

class Solution:
  '''
  The idea is to divide the array into (n-1) buckets: each bucket span a range
  of (hi-lo)/(n-1), and if the biggest pair gap happens inside the bucket, we
  will get the final sum greater than the possible sum of the array; hence the
  maximum gap only occurs to the max and min of the bucket comparing to the min and max of the neighboring bucket.
  '''
  def maximumGap(self, nums: List[int]) -> int:
    if len(nums) <= 1:
      return 0

    lo, hi, l = min(nums), max(nums), len(nums)
    if hi-lo <= 1:
      return hi-lo

    buckets = defaultdict(list)
    ans = 0

    # put numbers into buckets
    for n in nums:
      idx = l-1 if n == hi else (n-lo) * (l-1) // (hi-lo)
      buckets[idx].append(n)

    # print(buckets)

    # comparing min of the current bucket with the max of the previous bucket,
    # which must be one of the candidate answer
    last = -1
    for i in range(l):
      if i not in buckets:
        continue

      if last < 0:
        last = max(buckets[i])
        continue

      diff = min(buckets[i]) - last
      if diff > ans:
        ans = diff

      last = max(buckets[i])

    return ans
