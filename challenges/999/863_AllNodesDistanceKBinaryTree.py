'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''

from typing import List


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    stack = []
    vals = set()
    ans = []
    
    def collect(root, dist):
      if dist < 0 or not root:
        return
      
      if dist == 0:
        ans.append(root.val)
        return
      
      if root.left and root.left.val not in vals:
        collect(root.left, dist-1)
        
      if root.right and root.right.val not in vals:
        collect(root.right, dist-1)
    
    def walk(node):
      if not node:
        return False
      
      stack.append(node)
      vals.add(node.val)
      
      if node.val == target.val:
        idx = 0
        while k+idx >= 0 and len(stack)+idx > 0:
          # print('stack:', [n.val for n in stack])
          # print('collect:', stack[idx-1].val, k+idx)
          collect(stack[idx-1], k+idx)
          idx -= 1
          
        return True
      
      if walk(node.left) or walk(node.right):
        return True
      
      stack.pop()
      vals.discard(node.val)
      
      return False
      
    walk(root)
    
    return ans
        
        
  def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    stack = []
    ans = []
    last = None
    
    def find(root):
      if not root:
        return False
      
      stack.append(root)
      # print(root.val)
      
      if root.val == target.val:
        return True
      
      if find(root.left):
        return True
      
      if find(root.right):
        return True
      
      stack.pop()
      return False
    
    def add_node(root, dist):
      if not root:
        return
      
      if dist == 0:
        ans.append(root.val)
        return
      
      if root.left != last:
        add_node(root.left, dist-1)
        
      if root.right != last:
        add_node(root.right, dist-1)
      
    find(root)
    # print([t.val for t in stack])
    
    while stack and k >= 0:
      curr = stack[-1]
      add_node(curr, k)
      
      last = stack.pop()
      k -= 1
    
    return ans
      