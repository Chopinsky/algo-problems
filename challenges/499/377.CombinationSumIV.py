'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:

Input: nums = [9], target = 3
Output: 0

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
'''

class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    nums.sort()
    if target < nums[0]:
      return 0

    idx = 0
    counts = collections.defaultdict(int)
    counts[0] = 1

    for i in range(nums[0], target+1):
      cnt = 0

      if idx < len(nums) and i == nums[idx]:
        idx += 1

      for j in range(idx+1):
        if j >= len(nums):
          break

        n = counts[i-nums[j]]
        cnt += n if n > 0 else 0

      counts[i] = cnt

    return counts[target]