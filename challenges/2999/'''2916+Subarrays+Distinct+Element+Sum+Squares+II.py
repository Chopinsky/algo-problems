'''
2916. Subarrays Distinct Element Sum of Squares II

You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''

from typing import List


class Solution:
  def sumCounts(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    n = len(nums)
    tree = [0] * (4*n)
    lazy = [0] * (4*n)
    
    def merge_back(u, lo, hi):
      if not lazy[u]:
        return
      
      tree[u] += (hi-lo+1) * lazy[u]
      if lo < hi:
        # move down 1 level to the left
        lazy[2*u+1] += lazy[u]
        # move down 1 level to the right
        lazy[2*u+2] += lazy[u]
          
      # merged and reset
      lazy[u] = 0
    
    def update(u, lo, hi, i, j, val):
      merge_back(u, lo, hi)
          
      if lo > j or hi < i:
        return
      
      # inclusive interval
      if lo >= i and hi <= j:
        tree[u] += (hi-lo+1) * val
        if lo < hi:
          # left
          lazy[2*u+1] += val
          # right
          lazy[2*u+2] += val
          
        return
      
      mid = (lo + hi) // 2
      update(2*u+1, lo, mid, i, j, val)
      update(2*u+2, mid+1, hi, i, j, val)
      tree[u] = tree[2*u+1] + tree[2*u+2]
      
    def query(u, lo, hi, i, j):
      # no intersection
      if j < lo or i > hi:
        return 0
      
      merge_back(u, lo, hi)
      
      if lo >= i and hi <= j:
        return tree[u]
      
      mid = (lo + hi) // 2
      if i > mid:
        return query(2*u+2, mid+1, hi, i, j)
      
      if j <= mid:
        return query(2*u+1, lo, mid, i, j)
        
      return query(2*u+1, lo, mid, i, mid) + query(2*u+2, mid+1, hi, mid+1, j)
    
    squares = 1
    update(0, 0, n-1, n-1, n-1, 1)
    index = {}
    index[nums[-1]] = n-1
    res = 1
    
    for i in range(n-2, -1, -1):
      val = nums[i]
      j = index[val] if val in index else n
      
      # squares addition == RangeSum<2*Count+1>[i+1, j-1]+1 == 2*RangeSum[i+1, j-1] + (j-i)
      squares += (j-i) + 2*query(0, 0, n-1, i+1, j-1)
      res = (res + squares) % mod
      
      # add 1 to the RangeSum for [i, j-1]
      update(0, 0, n-1, i, j-1, 1)
      index[val] = i
      
    return res
        