'''
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Example 1:

Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:

Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def distributeCoins(self, root: Optional[TreeNode]) -> int:
    cnt = [0, 0]
    avg = 0
    steps = 0
    
    def count(root):
      if not root:
        return 
      
      cnt[0] += 1
      cnt[1] += root.val
      
      count(root.left)
      count(root.right)
      
    def assign(root):
      nonlocal steps
      if not root:
        return 0
      
      # from left
      dl = assign(root.left)
      
      # from right
      dr = assign(root.right)
      
      # from parent
      dp = dl + dr + (root.val - avg)
      
      steps += abs(dl) + abs(dr) + abs(dp)
      
      return dp
      
    count(root)
    avg = cnt[1] // cnt[0]
    
    assign(root)
    # print(cnt, avg)
    
    return steps // 2
    