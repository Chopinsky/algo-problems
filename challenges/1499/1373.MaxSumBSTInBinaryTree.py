'''
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:

Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.

Example 4:

Input: root = [2,1,3]
Output: 6

Example 5:

Input: root = [5,4,8,3,null,6,3]
Output: 7

Constraints:

The number of nodes in the tree is in the range [1, 4 * 10^4].
-4 * 10^4 <= Node.val <= 4 * 10^4
'''


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxSumBST(self, root: Optional[TreeNode]) -> int:
    max_bst_sum = 0
    
    def search(root: Optional[TreeNode]) -> List[int]:
      nonlocal max_bst_sum
      
      if not root:
        return (True, 0, None)
      
      sub_sum = root.val
      rng = [root.val, root.val]
      sub_is_bst = True
      
      if root.left:
        l_is_bst, ls, l_rng = search(root.left)
        if l_is_bst and l_rng and l_rng[1] < root.val:
          rng[0] = l_rng[0]
          sub_sum += ls
        else:
          sub_is_bst = False
        
      if root.right:
        r_is_bst, rs, r_rng = search(root.right)
        if r_is_bst and r_rng and r_rng[0] > root.val:
          rng[1] = r_rng[1]
          sub_sum += rs
        else:
          sub_is_bst = False
        
      # print(root.val, sub_is_bst, sub_sum, rng)
      if sub_is_bst:
        max_bst_sum = max(max_bst_sum, sub_sum)
        return (True, sub_sum, rng)
      
      return (False, 0, None)
      
    is_bst, s, _ = search(root)
    
    return max_bst_sum
      