'''
988. Smallest String Starting From Leaf

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example 1:

Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:

Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:

Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"

Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25

[4,0,1,1]
[0,1,2,3,4,3,4]
[25,1,3,1,3,0,2]
[2,2,1,null,1,0,null,0]
[2,0,1,null,null,0]
[3,9,20,null,null,15,7]
[25,1,null,0,0,1,null,null,null,0]
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    small = ['']
    
    def dfs(root, upper):
      if not root:
        if not small[0]:
          small[0] = upper
        else:
          small[0] = min(small[0], upper)
          
        # print(upper, small)
        return 
      
      nxt = str(chr(ord('a') + root.val)) + upper
      if not root.left:
        dfs(root.right, nxt)
        return 
      
      if not root.right:
        dfs(root.left, nxt)
        return
      
      dfs(root.left, nxt)
      dfs(root.right, nxt)
      
    dfs(root, '')
    
    return small[0]
        