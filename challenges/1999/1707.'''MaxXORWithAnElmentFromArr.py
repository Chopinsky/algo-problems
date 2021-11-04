'''
You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

Example 1:

Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

Example 2:

Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]

Constraints:

1 <= nums.length, queries.length <= 10^5
queries[i].length == 2
0 <= nums[j], xi, mi <= 10^9
'''


from typing import List
from bisect import bisect_left, bisect_right


class Node:
  def __init__(self):
    self.child = [None, None]
    
    
  def add(self, n: int):
    curr = self
    for i in range(30, -1, -1):
      bit = (n >> i) & 1
      # print("adding bit:", n, i, bit)
      if not curr.child[bit]:
        curr.child[bit] = Node()
        
      curr = curr.child[bit]
      
      
  def max_xor(self, n: int) -> int:
    curr = self
    ans = 0
    # print(n)
    
    for i in range(30, -1, -1):
      bit = (n >> i) & 1
      # print("xor", n, i, bit, curr.child)
      if curr.child[1^bit]:
        curr = curr.child[1^bit]
        ans |= 1 << i
        
      else:
        curr = curr.child[bit]
    
    return ans
    

class Solution:
  def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    nums.sort()
    ans = []
    
    for val, cap in queries:
      l, r = 0, bisect_right(nums, cap)
      bit = 1 << cap.bit_length()
      num = 0
      # print(l, r, bit)
      
      # find the "trie" node using bisect
      while bit:
        cut = bisect_left(nums, num+bit, l, r)
        if cut != r:
          if cut != l and val & bit:
            r = cut
          else:
            l = cut
            num += bit
        
        bit >>= 1
      
      ans.append(num^val if l < r else -1)
    
    return ans
    
    
  def maximizeXor0(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    ans = [0] * len(queries)
    q = [(d[1], d[0], i) for i, d in enumerate(queries)]
    idx = 0
    root = Node()
    
    q.sort()
    nums.sort()
    # print(q, nums)
    
    for cap, val, i in q:
      while idx < n and nums[idx] <= cap:
        root.add(nums[idx])
        idx += 1
        
      # print("post-add", cap, idx)
      if idx == 0:
        ans[i] = -1
      else:
        ans[i] = root.max_xor(val)
    
    return ans
  