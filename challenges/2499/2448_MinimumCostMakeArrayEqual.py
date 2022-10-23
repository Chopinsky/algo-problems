'''
2448. Minimum Cost to Make Array Equal

You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.

Constraints:

n == nums.length == cost.length
1 <= n <= 10^5
1 <= nums[i], cost[i] <= 10^6
'''

from typing import List


class Solution:
  def minCost(self, nums: List[int], cost: List[int]) -> int:
    if len(set(nums)) == 1:
      return 0
    
    arr = sorted(zip(nums, cost))
    prefix = []
    n = len(nums)
    
    for _, c in arr:
      if not prefix:
        prefix.append(c)
      else:
        prefix.append(c + prefix[-1])
      
    # print(arr, prefix)
    base = 0
    for i in range(1, n):
      base += (arr[i][0] - arr[0][0]) * arr[i][1]
      
    min_cost = base
    for i in range(1, n):
      delta = arr[i][0] - arr[i-1][0]
      plus = delta * prefix[i-1]
      minus = delta * (prefix[-1] - prefix[i-1])
      # print(base, delta, plus, minus)

      base += plus - minus
      min_cost = min(min_cost, base)
    
    return min_cost
  