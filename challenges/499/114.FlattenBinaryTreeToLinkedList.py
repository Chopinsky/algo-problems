'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

from typing import Union, Tuple, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    last = None
    
    def iterate(root):
      nonlocal last
      
      if not root:
        return
      
      # stack.append(root)
      l, r = root.left, root.right
      if last:
        last.left = None
        last.right = root
        
      last = root
      iterate(l)
      iterate(r)
      
    iterate(root)


  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def traverse(root: TreeNode) -> Union[None, Tuple[TreeNode, TreeNode]]:
      if not root:
        return None

      if not root.left and not root.right:
        return (root, root)

      ll = traverse(root.left) if root.left else None
      rr = traverse(root.right) if root.right else None

      head, tail = root, root
      root.left = None

      if ll and ll[0] and ll[1]:
        tail.right = ll[0]
        tail = ll[1]

      if rr and rr[0] and rr[1]:
        tail.right = rr[0]
        tail = rr[1]

      return (head, tail)

    traverse(root)
