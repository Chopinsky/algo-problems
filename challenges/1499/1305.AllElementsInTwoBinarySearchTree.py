'''
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-10^5 <= Node.val <= 10^5
'''


from typing import List


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

    
class Solution:
  def getAllElements0(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    values = []
    
    def getNodes(root: TreeNode):
      if not root:
        return

      stack = [root]
      while stack:
        node = stack.pop()
        if node:
          values.append(node.val)
          
        if node.left:
          stack.append(node.left)

        if node.right:
          stack.append(node.right)

    getNodes(root1)
    getNodes(root2)

    return sorted(values)
      
      
  def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    ans = []
    
    def flatten0(root: TreeNode) -> List[int]:
      if not root:
        return []
      
      return flatten(root.left) + [root.val] + flatten(root.right)
    
    def flatten(root: TreeNode) -> List[int]:
      if not root:
        return []
      
      stack = []
      res = []
      curr = root
      
      # add all left branches
      while curr:
        stack.append(curr)
        curr = curr.left
        
      # recursively add all
      while stack:
        curr = stack.pop()
        res.append(curr.val)
        
        if curr.right:
          curr = curr.right
          while curr:
            stack.append(curr)
            curr = curr.left
      
      return res
    
    a1 = flatten(root1)
    a2 = flatten(root2)
    i, j = 0, 0
    # print(a1, a2)
    
    while i < len(a1) or j < len(a2):
      if i >= len(a1):
        ans.extend(a2[j:])
        break
        
      if j >= len(a2):
        ans.extend(a1[i:])
        break
        
      if a1[i] <= a2[j]:
        ans.append(a1[i])
        i += 1
      else:
        ans.append(a2[j])
        j += 1
    
    return ans
    