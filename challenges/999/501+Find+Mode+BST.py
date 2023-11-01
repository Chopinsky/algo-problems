'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
'''

from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    ans = []
    if not root:
      return ans
    
    count = defaultdict(int)
    stack = [root]
    max_count = 0
    idx = 0

    while idx < len(stack):
      val = stack[idx].val
      count[val] += 1
      if stack[idx].left:
        stack.append(stack[idx].left)
        
      if stack[idx].right:
        stack.append(stack[idx].right)
        
      idx += 1
      max_count = max(max_count, count[val])
      
    # print(count, max_count)
    for val, cnt in count.items():
      if cnt != max_count:
        continue
        
      ans.append(val)
    
    return ans
        