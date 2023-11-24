'''
2265. Count Nodes Equal to Average of Subtree

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.

Example 1:

Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:

Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
'''

from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    count = [0]
    
    def traverse(root):
      if not root:
        return 0, 0
      
      val = root.val
      
      s0, c0 = traverse(root.left)
      s1, c1 = traverse(root.right)

      val += s0 + s1
      cnt = 1 + c0 + c1
      
      if root.val == val//cnt:
        count[0] += 1
        
      return val, cnt
      
    traverse(root)
        
    return count[0]
      

  def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    count = 0
    
    def iterate(node) -> Tuple:
      nonlocal count
      
      if not node:
        return 0, 0
      
      s0, c0 = iterate(node.left)
      s1, c1 = iterate(node.right)
      
      s = s0 + s1 + node.val
      c = c0 + c1 + 1
      
      if s//c == node.val:
        count += 1
        
      return s, c
      
    iterate(root)
    return count
  