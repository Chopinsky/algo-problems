'''
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 10 ** 5].
1 <= Node.val <= 9
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    def count(root, mask):
      if not root:
        return 0
      
      curr = mask ^ (1 << root.val)
      if not root.left and not root.right:
        return 1 if curr == 0 or bin(curr)[2:].count('1') == 1 else 0
      
      lc = count(root.left, curr)
      rc = count(root.right, curr)
      
      return lc + rc
    
    return count(root, 0)
        
  def pseudoPalindromicPaths(self, root: TreeNode) -> int:
    nums = [0] * 10
    count = [0]

    def traverse(root: TreeNode):
      if not root:
        return

      nums[root.val] += 1

      if not root.left and not root.right:
        # print(root.val, nums)

        odd = False
        done = True

        for n in nums:
          if n % 2 == 0:
            continue

          if not odd:
            odd = True
          else:
            done = False
            break

        if done:
          count[0] += 1

      else:
        traverse(root.left)
        traverse(root.right)

      nums[root.val] -= 1

    traverse(root)

    return count[0]
