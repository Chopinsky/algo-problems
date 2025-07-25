'''
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

Example 1:

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
Example 2:

Input: nums = [7,9,5,8,1,3]
Output: 1
Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.

Constraints:

nums.length == 3 * n
1 <= n <= 10^5
1 <= nums[i] <= 10^5
'''


from typing import List
from heapq import heapify, heappushpop, heappop, heappush


class Solution:
  def minimumDifference(self, v: List[int]) -> int:
    n = len(v)//3

    # for each closed range [0,n], ... [0,2n-1] find min. n elements
    # store their sum
    h = [-val for val in v[:n]]
    heapify(h)
    p0 = [-sum(h)]

    for i in range(n, 2*n):
      val = v[i]
      prefix = p0[-1]

      if -val > h[0]:
        prefix -= -heappop(h)
        heappush(h, -val)
        prefix += val

      p0.append(prefix)

    # for each range [n,3n], ... [2n,3n] find max. n elements
    ## store their sum
    h = [val for val in v[2*n:]]
    heapify(h)
    p1 = [sum(h)]

    for i in range(2*n-1, n-1, -1):
      val = v[i]
      prefix = p1[-1]

      if val > h[0]:
        prefix -= heappop(h)
        heappush(h, val)
        prefix += val

      p1.append(prefix)

    p1 = p1[::-1]

    # cost is sum-min(N[0:n-1]) + sum-max(N[n:3n-1]) - closed ranges
    # here P starts at n-1 and S[::-1] ends at n - hence zip directly
    return min(p-s for p, s in zip(p0, p1))

  def minimumDifference(self, nums: List[int]) -> int:
    n = len(nums) // 3
    if n == 1:
      return min(
        min(nums[0], nums[1])-nums[2], 
        nums[0]-max(nums[1], nums[2])
      )
    
    ls = sum(nums[:n])
    rs = 0
    
    right = set()
    lh = [-val for val in nums[:n]]
    rest = [(-val, n+i) for i, val in enumerate(nums[n:])]
    
    heapify(lh)
    heapify(rest)
    
    while len(right) < n:
      node = heappop(rest)
      rs += -node[0]
      right.add(node[1])
      
    diff = ls - rs
    # print('init', n, diff, ls, rs, [nums[i] for i in right], rest)
    
    # moving i-th element from the right to the left
    # and adjust the heaps accordingly
    for i in range(n, 2*n):
      val = nums[i]
      
      # if val is smaller, pop-then-push into the left
      # heap first, and update the left-side sums
      if val < -lh[0]:
        old_val = -heappushpop(lh, -val)
        ls += val - old_val
        
      # clear the rest heap if the head element is
      # moved to the left side already
      while rest and rest[0][1] <= i:
        heappop(rest)
        
      # if the element is removed from the right heap 
      if i in right and rest:
        right.discard(i)
        rs -= val
        
        # now take an element from the rest and add it
        # to the right
        node = heappop(rest)
        rs += -node[0]
        right.add(node[1])
        
      # print('iterate', i, val, diff, ls, rs, sorted([nums[i] for i in right]), rest)
      diff = min(diff, ls-rs)
    
      # no more elements left for grab
      if not rest:
        # print('out??', lh)
        break
        
    # print('end', ls, rs, right)
    return diff
    