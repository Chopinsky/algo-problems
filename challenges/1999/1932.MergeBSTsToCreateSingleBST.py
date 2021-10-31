'''
You are given n BST (binary search tree) root nodes for n separate BSTs stored in an array trees (0-indexed). Each BST in trees has at most 3 nodes, and no two roots have the same value. In one operation, you can:

Select two distinct indices i and j such that the value stored at one of the leaves of trees[i] is equal to the root value of trees[j].
Replace the leaf node in trees[i] with trees[j].
Remove trees[j] from trees.
Return the root of the resulting BST if it is possible to form a valid BST after performing n - 1 operations, or null if it is impossible to create a valid BST.

A BST (binary search tree) is a binary tree where each node satisfies the following property:

Every node in the node's left subtree has a value strictly less than the node's value.
Every node in the node's right subtree has a value strictly greater than the node's value.
A leaf is a node that has no children.

Example 1:

Input: trees = [[2,1],[3,2,5],[5,4]]
Output: [3,2,5,1,null,4]
Explanation:
In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
Delete trees[0], so trees = [[3,2,5,1],[5,4]].

In the second operation, pick i=0 and j=1, and merge trees[1] into trees[0].
Delete trees[1], so trees = [[3,2,5,1,null,4]].

The resulting tree, shown above, is a valid BST, so return its root.

Example 2:

Input: trees = [[5,3,8],[3,2,6]]
Output: []
Explanation:
Pick i=0 and j=1 and merge trees[1] into trees[0].
Delete trees[1], so trees = [[5,3,8,2,6]].

The resulting tree is shown above. This is the only valid operation that can be performed, but the resulting tree is not a valid BST, so return null.

Example 3:

Input: trees = [[5,4],[3]]
Output: []
Explanation: It is impossible to perform any operations.

Example 4:

Input: trees = [[2,1,3]]
Output: [2,1,3]
Explanation: There is only one tree, and it is already a valid BST, so return its root.

Constraints:

n == trees.length
1 <= n <= 5 * 10^4
The number of nodes in each tree is in the range [1, 3].
Each node in the input may have children but no grandchildren.
No two roots of trees have the same value.
All the trees in the input are valid BSTs.
1 <= TreeNode.val <= 5 * 10^4.
'''


from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def canMerge(self, trees: List[TreeNode]) -> TreeNode:
    if not trees:
      return None
    
    n = len(trees)
    if n == 1:
      return trees[0]
    
    leaf_vals = set()
    leaves = {}
    
    for i, t in enumerate(trees):
      if t.left:
        leaf_vals.add(t.left.val)
        
      if t.right:
        leaf_vals.add(t.right.val)
        
    root = None
    for i, t in enumerate(trees):
      if t.val in leaf_vals:
        # dual leaves
        if t.val in leaves:
          return None
        
        leaves[t.val] = i
        continue
        
      # dual root -- not going to merge
      if root:
        return None
      
      root = t
      
    # print(root.val, leaves)
    # not a single root that won't find the leaf to
    # belong to, won't form a valid BST
    if not root:
      return None
    
    def merge(root: TreeNode, low: int, high: int):
      if not root:
        return
      
      if root.left and (root.left.val in leaves):
        # print('left node', root.left)
        curr = root.left
        idx = leaves[curr.val]
        t = trees[idx]
        
        if not t:
          # print('l1', root.val, curr.val, low, high)
          return 
        
        # not in the range
        if t.left and t.left.val <= low:
          # print('l2', root.val, curr.val, low, high)
          return

        if t.right and t.right.val >= min(root.val, high):
          # print('l3', root.val, curr.val, low, high)
          return

        # take this tree and merge
        trees[idx] = None
        curr.left = t.left
        curr.right = t.right
        # print('taking out', idx, curr)

        # merge(curr.left, low, min(high, curr.val))
        # merge(curr.right, max(low, curr.val), min(high, root.val))
        merge(curr, low, min(high, root.val))
          
      if root.right and (root.right.val in leaves):
        # print('right node', root.right)
        curr = root.right
        idx = leaves[curr.val]
        t = trees[idx]
        
        if not t:
          # print('r1', root.val, curr.val, low, high)
          return 
        
        # t.left out of the range
        if t.left and t.left.val <= max(low, root.val): 
          # print('r2', root.val, curr.val, low, high)
          return 

        # t.right out of the range
        if t.right and t.right.val >= high:
          # print('r3', root.val, curr.val, low, high)
          return

        # take this tree and merge
        trees[idx] = None
        curr.left = t.left
        curr.right = t.right

        # merge(curr.left, max(low, root.val), min(high, curr.val))
        # merge(curr.right, max(low, curr.val), high)
        merge(curr, max(low, root.val), high)
    
    merge(root, -math.inf, math.inf)
    
    # validate the tree set and make sure all other
    # trees have been merged
    for t in trees:
      if t == root:
        continue
        
      # there are BSTs that can't merge into the single BST
      if t:
        # print('v', t.val, trees)
        return None
    
    return root
  