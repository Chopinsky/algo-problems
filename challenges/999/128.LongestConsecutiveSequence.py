'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 10 ** 5
-10 ** 9 <= nums[i] <= 10 ** 9
'''

from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0

    nums = set(nums)
    count = 1

    for n in nums:
      # already tallied
      if n-1 in nums:
        continue

      # count consequtive numbers
      c = 1
      while n+1 in nums:
        c += 1
        n += 1

      count = max(c, count)

    return count

  def longestConsecutive1(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0

    num_dict = {}

    for n in nums:
      if n in num_dict:
        continue

      l, r = n, n

      if n-1 in num_dict:
        l = n-1
        num_dict[n-1][1] = n

      if n+1 in num_dict:
        r = n+1
        num_dict[n+1][0] = n

      num_dict[n] = [l, r]

    count = 1
    for n, links in num_dict.items():
      if links[0] != n:
        continue

      c = 1
      while links[1] != n:
        c += 1
        n = links[1]
        links = num_dict[n]

      count = max(count, c)

    return count
