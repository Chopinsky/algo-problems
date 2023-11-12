'''
2935. Maximum Strong Pair XOR II

You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.

Return the maximum XOR value out of all possible strong pairs in the array nums.

Note that you can pick the same integer twice to form a pair.

Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.
Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.
Example 3:

Input: nums = [500,520,2500,3000]
Output: 1020
Explanation: There are 6 strong pairs in the array nums: (500, 500), (500, 520), (520, 520), (2500, 2500), (2500, 3000) and (3000, 3000).
The maximum XOR possible from these pairs is 500 XOR 520 = 1020 since the only other non-zero XOR value is 2500 XOR 3000 = 636.

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 2^20 - 1
'''

from typing import List


class Solution:
  '''
  step-1) sort the array, then strong pairs == subarray of [i, j], where nums[j] is the biggest number 
  in the subarray that's equal to or smaller than 2*nums[i]; iterate with index-i for the original
  array, and query for the maximum XOR for the subarray --> "moving window"

  step-2) to query the maximum XOR within the subarray in O(log(n)), we need to build the "binary trie",
  that is, convert each new value added to the moving window subarray into the binary trie in its binary
  form, and query the trie with the "reverse" route choice: if the trie node contains the opposite value 
  (i.e., 1 for 0 and 0 for 1) for the digit at level-k, i.e., 1 - (value & (1 << k)) exists at this binary
  shift, then we go to that node; otherwise, continue with the node that exists; repeat until we reach the 
  bottom of the trie, that number will make the biggest XOR for any `value ^ subarray_element` in the subarray
  '''
  def maximumStrongPairXor(self, nums: List[int]) -> int:
    def insert(node, val, level):
      mask = 1 << level
      d = 0 if val&mask == 0 else 1
      
      if level == 0:
        node[d] = val
        return

      if d not in node:
        node[d] = {}
        
      insert(node[d], val, level-1)
    
    def delete(node, val, level):
      mask = 1 << level
      d = 0 if val&mask == 0 else 1
      
      if d not in node:
        return
      
      if level == 0:
        del node[d]
        return
      
      delete(node[d], val, level-1)
      
      if len(node[d]) == 0:
        del node[d]
    
    def query(node, val, level):
      if len(node) == 0:
        return val
      
      mask = 1 << level
      d = 0 if val&mask == 0 else 1
      rd = 1 - d
      
      if level == 0:
        return node[rd] if rd in node else node[d]
      
      return query(node[rd], val, level-1) if rd in node else query(node[d], val, level-1)

    nums.sort()
    xor, j = 0, 0
    n = len(nums)
    root = {}
    
    for i in range(n):
      val = nums[i]
      if i > 0 and val == nums[i-1]:
        continue
      
      while j < n and nums[j]-val <= val:
        insert(root, nums[j], 20)
        j += 1
        
      delete(root, val, 20)
      pair = query(root, val, 20)
      
      # print('post:', val, root)
      # print('pair:', (val, pair), val^pair)
      xor = max(xor, val^pair)
    
    return xor
        