'''
1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    vals = set(to_delete)
    ans = []
    
    def remove(node, to_add: bool):
      if not node:
        return None
      
      if node.val in vals:
        node.left = remove(node.left, True)
        node.right = remove(node.right, True)
        return None

      node.left = remove(node.left, False)
      node.right = remove(node.right, False)
      
      if to_add:
        ans.append(node)
        
      return node
      
    remove(root, True)
    
    return ans
        