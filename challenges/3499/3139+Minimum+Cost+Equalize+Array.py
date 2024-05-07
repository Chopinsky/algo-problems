'''
3139. Minimum Cost to Equalize Array

You are given an integer array nums and two integers cost1 and cost2. You are allowed to perform either of the following operations any number of times:

Choose an index i from nums and increase nums[i] by 1 for a cost of cost1.
Choose two different indices i, j, from nums and increase nums[i] and nums[j] by 1 for a cost of cost2.
Return the minimum cost required to make all elements in the array equal.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: nums = [4,1], cost1 = 5, cost2 = 2

Output: 15

Explanation:

The following operations can be performed to make the values equal:

Increase nums[1] by 1 for a cost of 5. nums becomes [4,2].
Increase nums[1] by 1 for a cost of 5. nums becomes [4,3].
Increase nums[1] by 1 for a cost of 5. nums becomes [4,4].
The total cost is 15.

Example 2:

Input: nums = [2,3,3,3,5], cost1 = 2, cost2 = 1

Output: 6

Explanation:

The following operations can be performed to make the values equal:

Increase nums[0] and nums[1] by 1 for a cost of 1. nums becomes [3,4,3,3,5].
Increase nums[0] and nums[2] by 1 for a cost of 1. nums becomes [4,4,4,3,5].
Increase nums[0] and nums[3] by 1 for a cost of 1. nums becomes [5,4,4,4,5].
Increase nums[1] and nums[2] by 1 for a cost of 1. nums becomes [5,5,5,4,5].
Increase nums[3] by 1 for a cost of 2. nums becomes [5,5,5,5,5].
The total cost is 6.

Example 3:

Input: nums = [3,5,3], cost1 = 1, cost2 = 3

Output: 4

Explanation:

The following operations can be performed to make the values equal:

Increase nums[0] by 1 for a cost of 1. nums becomes [4,5,3].
Increase nums[0] by 1 for a cost of 1. nums becomes [5,5,3].
Increase nums[2] by 1 for a cost of 1. nums becomes [5,5,4].
Increase nums[2] by 1 for a cost of 1. nums becomes [5,5,5].
The total cost is 4.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= cost1 <= 10^6
1 <= cost2 <= 10^6
'''

from typing import List

class Solution:
  '''
  the idea is that if the `head_ops = biggest_number - smallest_number` is equal or smaller to the 
  increases of all the rest of the numbers to `biggest_number` with `rest_ops`, aka `head_ops <= rest_ops`,
  then we can pair all operations together using `cost2`, or at most 1 number is left out, where we 
  perform op1 with `cost1`;

  if `head_ops > rest_ops`, then we can pair all ops between the `smallest_number` with the rest
  of the numbers, but then using `head_ops - rest_ops` of op1 with `cost1` to even the array out;
  then we keep growing the height of the array by 1, calculate the cost using the same algo, until
  `head_ops <= rest_ops`, then we can use first part of the algo to get the min-cost; then we just
  take the minimum cost of all these possible senarios;
  '''
  def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
    n = len(nums)
    nums.sort()
    mod = 10**9 + 7
    
    if n <= 2:
      return (cost1 * (nums[-1]-nums[0])) % mod
    
    diff = [nums[-1]-nums[i] for i in range(n)]
    rest = sum(diff[1:])
    # print('init:', diff, rest)
    
    if 2*cost1 <= cost2:
      return (cost1*(diff[0]+rest)) % mod
    
    def calc_cost(head: int, rest: int):
      if head == rest:
        return cost2*head

      if head > rest:
        return cost1*(head-rest) + cost2*rest

      # head < rest
      total = head + rest
      if total % 2 == 0:
        return cost2*total//2

      # has 1 unpairable integer
      c0 = cost1 + cost2*(total-1)//2
      if n % 2 == 0:
        return c0

      # can add extra layer to make all equal and paired, aka forming 
      # the total of `(total-1)//2 + (n+1)//2` pairs:
      c1 = c0 - cost1 + cost2*(n+1)//2

      return min(c0, c1)
    
    head = diff[0]
    min_cost = calc_cost(head, rest)
    
    # keep raising the height until an optimized solution can be achieved
    while head > rest:
      head += 1
      rest += n-1
      c0 = calc_cost(head, rest)
      min_cost = min(min_cost, c0)
      # print('grow:', (head, rest), c0)
      
    return min_cost % mod
        