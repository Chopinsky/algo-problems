# Definition for a binary tree node.
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 10 ** 5].
-10 ** 9 <= Node.val <= 10 ** 9
All Node.val are unique.
p != q
p and q will exist in the tree.
'''

from typing import Optional, Tuple


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    found = False
    
    def find(root):
      nonlocal found
      
      if not root or found:
        return None
      
      l = find(root.left)
      r = find(root.right)
      cnt = 1 if (root.val == p.val or root.val == q.val) else 0
      
      if l:
        cnt += 1
        
      if r:
        cnt += 1
        
      # print(root.val, cnt)
      if cnt == 2:
        found = True
        return root
      
      if cnt == 1:
        if not l and not r:
          return root
        
        return l if l is not None else r
        
      return None
    
    return find(root)


  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
      return root
    
    def walk(root: TreeNode) -> Tuple[int, Optional[TreeNode]]:
      if not root:
        return (0, None)
      
      status = 0
      if root.val == p.val or root.val == q.val:
        status += 1
      
      left, lp = walk(root.left)
      right, rp = walk(root.right)
      
      if left == 2 and lp:
        return (left, lp)
      
      if right == 2 and rp: 
        return (right, rp)
      
      status += left + right
      if status == 2:
        return (2, root)
      
      return (status, None)
    
    _, parent = walk(root)
    
    return parent


  def lowestCommonAncestor0(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def check(root: TreeNode):
      pf = (root.val == p.val)
      qf = (root.val == q.val)
      
      if root.left:
        (lc_pf, lc_qf, node) = check(root.left)
        if node is not None:
          return (True, True, node)
          
        pf = pf or lc_pf
        qf = qf or lc_qf
        
      if root.right:
        (rc_pf, rc_qf, node) = check(root.right)
        if node is not None:
          return (True, True, node)
          
        pf = pf or rc_pf
        qf = qf or rc_qf
        
      if pf and qf:
        return (True, True, root)
      
      return (pf, qf, None)
        
    (_, _, node) = check(root)
    
    return node
  