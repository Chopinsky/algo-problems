'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
    
class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    max_val = root.val
    
    def iterate(root: Optional[TreeNode], min_pre: int, curr_pre: int) -> int:
      nonlocal max_val

      if not root:
        return -math.inf
      
      if not root.left and not root.right:
        max_val = max(max_val, root.val)
        # print(root.val, max_val)
        return root.val
      
      pre_max = max(0, curr_pre - min_pre)
      curr_pre += root.val
      min_pre = min(min_pre, curr_pre)
      max_self = root.val if root.val >= 0 else 0
      
      left = iterate(root.left, min_pre, curr_pre)
      right = iterate(root.right, min_pre, curr_pre)
      
      max_val = max(
        max_val, 
        root.val,           # lone node
        left + max_self,    # partial chain - left alone
        right + max_self,   # partial chain - right alone
        pre_max + root.val, # partial chain - top alone
        left + root.val + right,    # l+mid+r
        pre_max + root.val + left,  # l+mid+top
        pre_max + root.val + right, # r+mid+top
      )
      
      # print(root.val, max_val, left, right, pre_max)
      
      # return max(root.val+left, root.val+right)
      return max(
        root.val,
        left + root.val,
        right + root.val,
      )
    
    iterate(root, 0, 0)
    
    return max_val
