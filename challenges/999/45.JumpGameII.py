'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]

Output: 2

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10 ** 5
'''

class Solution:
  def jump(self, nums: List[int]) -> int:
    count = 0
    end = 0
    far = 0
    n = len(nums)

    for i in range(n-1):
      # in the region we can reach between jump `count-1` and `count`, update
      # the furthest bound we can reach from anywhere inside the region
      far = max(far, i+nums[i])

      # if we have reach the end of this region that's reachable from jump `count-1`
      # to jump `count`, now set the next region's bound (i.e. update the `end`)
      if i == end:
        count += 1
        end = far

        # we can reach the end from this jump, done.
        if end >= n-1:
          break

    return count


  def jump1(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [math.inf] * n
    dp[0] = 0

    for i in range(n-1):
      forward = nums[i]
      if forward == 0:
        continue

      next = dp[i]+1
      for d in range(1, forward+1):
        if i+d >= n:
          break

        if next < dp[i+d]:
          dp[i+d] = next

    return dp[-1]
