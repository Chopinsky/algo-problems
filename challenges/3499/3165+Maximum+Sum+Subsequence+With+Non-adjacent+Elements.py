'''
3165. Maximum Sum of Subsequence With Non-adjacent Elements

You are given an array nums consisting of integers. You are also given a 2D array queries, where queries[i] = [posi, xi].

For query i, we first set nums[posi] equal to xi, then we calculate the answer to query i which is the maximum sum of a subsequence of nums where no two adjacent elements are selected.

Return the sum of the answers to all queries.

Since the final answer may be very large, return it modulo 109 + 7.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [3,5,9], queries = [[1,-2],[0,-3]]

Output: 21

Explanation:
After the 1st query, nums = [3,-2,9] and the maximum sum of a subsequence with non-adjacent elements is 3 + 9 = 12.
After the 2nd query, nums = [-3,-2,9] and the maximum sum of a subsequence with non-adjacent elements is 9.

Example 2:

Input: nums = [0,-1], queries = [[0,-5]]

Output: 0

Explanation:
After the 1st query, nums = [-5,-1] and the maximum sum of a subsequence with non-adjacent elements is 0 (choosing an empty subsequence).

Constraints:

1 <= nums.length <= 5 * 10^4
-10^5 <= nums[i] <= 10^5
1 <= queries.length <= 5 * 10^4
queries[i] == [posi, xi]
0 <= posi <= nums.length - 1
-10^5 <= xi <= 10^5
'''

from typing import List

class Solution:
  '''
  use segment tree to store the maximum values for different settings of the subsequence in the given range:
  t0: _|__|_ (do not use value at either end)
  t1: _|___| (do not use left end)
  t2: |___|_ (do not use right end)
  t3: |____| (can use both ends)

  and the state transition matrix can be obtained as:
    curr_t0 = max(0, left_t1+right_t0, left_t0+right_t2)
    curr_t1 = max(0, left_t1+right_t1, left_t0+right_t3)
    curr_t2 = max(0, left_t3+right_t0, left_t2+right_t2)
    curr_t3 = max(0, left_t3+right_t1, left_t2+right_t3)

  where left, right is the children node of the current node, and if current node covers [left, right], then
  middle = (left + right) // 2, and the left node covers [left, mid] and the right node covers [mid+1, right]
  '''
  def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)
    mod = 10**9 + 7
    sums = 0
    
    if n <= 2:
      for idx, val in queries:
        nums[idx] = val
        sums += max(0, max(nums))
        
      return sums % mod
    
    tree = [None]*(4*n)
    
    # [left, right, no_ends, no_head, no_tail, both]
    tree[1] = [0, n-1, 0, 0, 0, 0]
    
    def build(i: int, val: int):
      idx = 1
      curr = tree[idx]
      stack = [1]
      
      while curr[0] != curr[1]:
        mid = (curr[0] + curr[1]) // 2
        
        if not tree[2*idx]:
          tree[2*idx] = [curr[0], mid, 0, 0, 0, 0]
          
        if not tree[2*idx+1]:
          tree[2*idx+1] = [mid+1, curr[1], 0, 0, 0, 0]
          
        if i <= mid:
          idx = 2*idx
        else:
          idx = 2*idx + 1
          
        curr = tree[idx]
        stack.append(idx)
        
      while stack:
        idx = stack.pop()
        update(idx, val)
      
    def update(i:int, val: int):
      if i >= len(tree):
        return
      
      node = tree[i]
      if node[0] == node[1]:
        node[2] = 0
        node[3] = 0
        node[4] = 0
        node[5] = max(0, val)
        return
      
      left = tree[2*i]
      right = tree[2*i+1]
      # print('update:', node, left, right)
      
      node[2] = max(
        0,
        left[3] + right[2],
        left[2] + right[4],
      )
      
      node[3] = max(
        0,
        left[3] + right[3],
        left[2] + right[5],
      )
      
      node[4] = max(
        0,
        left[5] + right[2],
        left[4] + right[4],
      )
      
      node[5] = max(
        0,
        left[5] + right[3],
        left[4] + right[5],
      )
    
    # initialize the tree
    for i in range(n):
      build(i, nums[i])
    
    # print('init:', tree)
    
    for idx, val in queries:
      build(idx, val)
      sums = (sums + tree[1][5]) % mod
    
    return sums
        