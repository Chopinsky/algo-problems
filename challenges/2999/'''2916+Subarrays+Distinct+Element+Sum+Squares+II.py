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


class Node:
  def __init__(self, lo: int, hi: int):
    self.lo = lo
    self.hi = hi
    self.val = 0
    self.lazy = 0

    if lo+1 < hi:
      mid = (lo+hi) // 2
      self.l = Node(lo, mid)
      self.r = Node(mid, hi)

  def update(self, val: int):
    self.lazy += val
    self.val += val * (self.hi - self.lo)

  def query(self, lo: int, hi: int) -> int:
    if lo <= self.lo and self.hi <= hi:
      res = self.val
      self.update(1)
      return res

    mid = (self.lo + self.hi) // 2
    res = 0
    
    self.l.update(self.lazy)
    self.r.update(self.lazy)
    self.lazy = 0

    if lo < mid:
      res += self.l.query(lo, hi)
    
    if mid < hi:
      res += self.r.query(lo, hi)

    self.val = self.l.val + self.r.val
    return res


class Solution:
  def sumCounts(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    last = {}
    tree = Node(0, len(nums))
    res = 0
    curr = 0

    for i, val in enumerate(nums):
      last_idx = last.get(val, -1) + 1
      curr = (curr + (i-last_idx+1) + 2*tree.query(last_idx, i+1)) % mod
      res += curr
      last[val] = i

    return res % mod

  def sumCounts(self, nums: List[int]) -> int:
    n = len(nums)
    t = [0] * (4*n)
    lz = [0] * (4*n)

    def push(x: int, l: int, r: int):
      if not lz[x]:
        return

      # push down the lz values tree
      m = (l + r) // 2
      
      # l-child
      t[2*x] += lz[x] * (m-l+1)
      lz[2*x] += lz[x]

      # r-child
      t[2*x+1] += lz[x] * (r-m)
      lz[2*x+1] += lz[x]

      # reset lz
      lz[x] = 0

    def update(x: int, l: int, r: int, a: int, b: int):
      # outside the bound, nothing to be done
      if b < l or a > r:
        return

      # inclusive, update
      if a <= l and r <= b:
        t[x] += r-l+1
        lz[x] += 1
        return

      # need to update the partial tree
      push(x, l, r)
      m = (l+r) // 2

      # update the subtree
      update(2*x, l, m, a, b)
      update(2*x+1, m+1, r, a, b)
      t[x] = t[2*x] + t[2*x+1]

    def query(x: int, l: int, r: int, a: int, b: int) -> int:
      if b < l or a > r:
        return 0

      if a <= l and r <= b:
        return t[x]

      push(x, l, r)
      m = (l+r) // 2
      return query(2*x, l, m, a, b) + query(2*x+1, m+1, r, a, b)

    mod = 10**9 + 7
    sq = 0
    ans = 0
    last = [-1] * 100001

    for i in range(n):
      p = last[nums[i]]
      s = query(1, 0, n-1, p+1, i)
      sq = (sq + 2*(s%mod) + (i-p)) % mod
      update(1, 0, n-1, p+1, i)
      ans = (ans + sq) % mod
      last[nums[i]] = i

    return ans

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
        