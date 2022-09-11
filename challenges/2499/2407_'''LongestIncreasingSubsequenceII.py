'''
2407. Longest Increasing Subsequence II

You are given an integer array nums and an integer k.

Find the longest subsequence of nums that meets the following requirements:

The subsequence is strictly increasing and
The difference between adjacent elements in the subsequence is at most k.
Return the length of the longest subsequence that meets the requirements.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
Output: 5
Explanation:
The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.
Example 2:

Input: nums = [7,4,5,1,8,12,4,7], k = 5
Output: 4
Explanation:
The longest subsequence that meets the requirements is [4,5,8,12].
The subsequence has a length of 4, so we return 4.
Example 3:

Input: nums = [1,5], k = 1
Output: 1
Explanation:
The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i], k <= 10^5
'''

from typing import List


# this version is TLE
class TreeNode:
  def __init__(self, l: int, h: int):
    self.l = l
    self.h = h
    self.longest = 0
    self.left = None
    self.right = None
    
    
  def query(self, l: int, h: int) -> int:
    # out of the bound, default to 0
    if self.l > h or self.h < l:
      return 0
    
    # included in the query range, done
    if l <= self.l and self.h <= h:
      return self.longest
    
    mid = (self.l+self.h)//2
    longest = 0
    
    if self.left and l <= mid:
      longest = max(longest, self.left.query(max(l, self.l), min(h, mid)))
    
    if self.right and h >= mid+1:
      longest = max(longest, self.right.query(max(mid+1, l), min(h, self.h)))
    
    return longest
  
  
  def update(self, val: int, ln: int):
    if self.longest < ln:
      self.longest = ln
    
    # at the leaf, we're done
    if self.l == self.h:
      # print('leaf:', level)
      return
    
    mid = (self.l+self.h)//2
    if val <= mid:
      # down the tree to the left branch
      if not self.left:
        self.left = TreeNode(self.l, mid)
        
      self.left.update(val, ln)
      
    else:
      # down the tree to the right branch
      if not self.right:
        self.right = TreeNode(mid+1, self.h)
        
      self.right.update(val, ln)


class Node:
  def __init__(self, max_val):
    self.n = max_val
    self.tree = [0] * (2*max_val)
    
    
  def query(self, l, r):
    # padding to the leaf
    l += self.n
    r += self.n
    ans = 0
    
    while l < r:
      if l & 1:
        ans = max(ans, self.tree[l])
        l += 1
      
      if r & 1:
        r -= 1
        ans = max(ans, self.tree[r])
        
      l >>= 1
      r >>= 1
      
    return ans
  
  
  def update(self, i, val):
    # padding to the leaf
    i += self.n
    self.tree[i] = val
    
    while i > 1:
      i >>= 1
      self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
  

class Solution:
  def lengthOfLIS(self, nums: List[int], k: int) -> int:
    n, ans = max(nums), 1
    tree = Node(n)
    
    for val in nums:
      val -= 1
      chain = 1+tree.query(max(0, val-k), val)
      ans = max(ans, chain)      
      tree.update(val, chain)
      
    return ans
    
    
  def lengthOfLIS0(self, nums: List[int], k: int) -> int:
    low, high = min(nums), max(nums)
    if low == high:
      return 1
    
    # root = TreeNode(low, high)
    root = [low, high, 0, None, None]
    
    def query(src: List, l: int, h: int) -> int:
      if src[0] > h or src[1] < l:
        return 0
      
      if l <= src[0] and src[1] <= h:
        return src[2]
      
      mid = (src[0]+src[1]) // 2
      longest = 0
      
      if src[3] and l <= mid:
        longest = max(longest, query(src[3], max(l, src[0]), min(mid, h)))
        
      if src[4] and h >= mid+1:
        longest = max(longest, query(src[4], max(mid+1, l), min(src[1], h)))
      
      return longest
    
    def update(src: List, val: int, ln: int):
      src[2] = max(src[2], ln)
      if src[0] == src[1]:
        return
      
      mid = (src[0]+src[1])//2
      if val <= mid:
        if not src[3]:
          src[3] = [src[0], mid, 0, None, None]
          
        update(src[3], val, ln)
        
      else:
        if not src[4]:
          src[4] = [mid+1, src[1], 0, None, None]
          
        update(src[4], val, ln)
    
    dp = {}
    for val in nums:
      if val == low:
        dp[val] = 1
        
      else:
        # dp[val] = max(dp.get(val, 0), 1+root.query(max(low, val-k), max(low, val-1)))
        dp[val] = max(dp.get(val, 0), 1+query(root, max(low, val-k), max(low, val-1)))
  
      # root.update(val, dp[val])
      update(root, val, dp[val])

    # print(dp)
    return max(dp.values())
    