'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    last_level = 0
    last_cnt = 0
    total = 0
    
    def walk(root, lvl):
      nonlocal last_level, last_cnt, total
      
      # we're at a leaf
      if not root.left and not root.right:
        # we're at the true last level
        if last_cnt > 0 and lvl != last_level:
          full_cnt = (1 << lvl) - 1
          total = full_cnt - 2*last_cnt
          # print(0, lvl, full_cnt)
          return False
          
        # we're at the right most leaf
        last_level = lvl
        last_cnt += 1
        total = (1 << lvl) - 1
          
        return True
      
      # we're at a parent of the true leaf
      if root.left and not root.right:
        full_cnt = (1 << (lvl+1)) - 1
        total = full_cnt - (2*last_cnt) - 1
        # print(1, lvl, full_cnt)
        return False
      
      return walk(root.right, lvl+1) and walk(root.left, lvl+1)
      
    walk(root, 1)
    
    return total
    
    
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    curr = root
    depth = 0
    
    while curr and curr.left:
      curr = curr.left
      depth += 1
      
    if not depth:
      return 1
      
    def search(idx: int) -> bool:
      curr = root
      l, r = 0, (1<<depth)-1
      
      for i in range(depth):
        mid = (l + r) // 2
        if idx > mid:
          curr = curr.right
          l = mid+1
        else:  
          curr = curr.left
          r = mid
          
      return curr != None
    
    l, r = 1, (1<<depth)-1
    
    while l <= r:
      mid = (l + r) // 2
      
      if search(mid):
        l = mid+1
      else:  
        r = mid-1
        
    return (1<<depth) - 1 + l
    
    
    
  def countNodes0(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    if not root.left:
      return 1
    
    if not root.right:
      return 2
    
    leaf = [0, 1]
    seen_leaf = False
    stack = [(root.left, 1, 2), (root.right, 1, 3)]
    
    while stack:
      curr, level, idx = stack.pop()
      if curr.right and curr.left:
        stack.append((curr.left, level+1, 2*idx))
        stack.append((curr.right, level+1, 2*idx+1))
        continue
        
      if curr.left:
        stack.append((curr.left, level+1, 2*idx))
        continue
        
      # leaf node in the next level, answer
      if seen_leaf and level > leaf[0]:
        leaf[0] = level
        leaf[1] = idx
        break
      
      # leaf node to the left
      if level == leaf[0]:
        continue
        
      leaf[0] = level
      leaf[1] = idx
      seen_leaf = True
    
    return leaf[1]