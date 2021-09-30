'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [0]
Output: 0

Example 3:

Input: nums = [2,4]
Output: 6

Example 4:

Input: nums = [8,10,2]
Output: 10

Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
'''


from typing import List


class Node:
  def __init__(self):
    self.children = [None, None]
    self.count = 0
    
    
  def add(self, n: int):
    curr = self
    
    for i in range(31, -1, -1):
      bit = (n >> i) & 1
      if not curr.children[bit]:
        curr.children[bit] = Node()
        
      curr = curr.children[bit]
      curr.count += 1
    
    
  def get_max(self, n: int) -> int:
    curr, ans = self, 0
    
    # go through the trie and find the max-diff number
    for i in range(31, -1, -1):
      bit = (n >> i) & 1
      if curr.children[1^bit]:
        curr = curr.children[1^bit]
        ans |= 1 << i
      else:
        curr = curr.children[bit]
        
    return ans
  

class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
    root = Node()
    for n in nums:
      root.add(n)
      
    ans = 0
    for n in nums:
      ans = max(ans, root.get_max(n))
      
    return ans
    
  def findMaximumXOR0(self, nums: List[int]) -> int:
    ans = 0
    mask = 0
    
    # build the answer bottom up
    for i in range(31, -1, -1):
      mask |= 1 << i
      nxt = ans | (1 << i)
      seen = set()
      
      for n in nums:
        # found the pair, done
        if (n&mask) ^ nxt in seen:
          ans = nxt
          break
          
        # update the seen part
        seen.add(n & mask)
        
    return ans