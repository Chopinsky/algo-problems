'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 10^5
'''

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def balanceBST(self, root: TreeNode) -> TreeNode:
    stack = []
    
    def flatten(node):
      if not node:
        return
      
      flatten(node.left)
      node.left = None
      
      stack.append(node)
      
      flatten(node.right)
      node.right = None
      
    def rebuild(arr):
      if not arr:
        return None
      
      n = len(arr)
      if n == 1:
        return arr[0]
        
      idx = n//2
      root = arr[idx]
      root.left = rebuild(arr[:idx])
      root.right = rebuild(arr[idx+1:])
      
      return root
    
    flatten(root)
    # print(stack)
    
    return rebuild(stack)
    
  def balanceBST(self, root: TreeNode) -> TreeNode:
    arr = []
    def to_arr(root):
      if not root:
        return
      
      to_arr(root.left)
      arr.append(root)
      to_arr(root.right)
      
      root.left = None
      root.right = None
      
      return
    
    def rebuild(i: int, j: int):
      if i == j:
        return arr[i]
      
      k = (i + j) // 2
      if k > i:
        arr[k].left = rebuild(i, k-1)
        
      if k < j:
        arr[k].right = rebuild(k+1, j)
        
      return arr[k]
    
    to_arr(root)
    return rebuild(0, len(arr)-1)
  