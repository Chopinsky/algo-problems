'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
'''


from typing import List
from math import inf


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  @staticmethod
  def build_tree(src: List[int]) -> TreeNode:
    root = TreeNode(src[0])
    stack, nxt = [root], []
    idx = 1

    while stack:
      for node in stack:
        if idx >= len(src):
          break

        node.left = TreeNode(src[idx])
        if node.left:
          nxt.append(node.left)

        idx += 1

        node.right = TreeNode(src[idx])
        if node.right:
          nxt.append(node.right)

        idx += 1

      stack, nxt = nxt, stack
      nxt.clear()

    # Solution.print_tree(root)
    return root

  @staticmethod
  def print_tree(node: TreeNode):
    if not node:
      return 

    Solution.print_tree(node.left)
    print(node.val)
    Solution.print_tree(node.right)

  def closest_value(self, root: TreeNode, target: float, k: int) -> List[int]:
    small = []
    big = []

    def search(root: TreeNode, low: int, high: int):
      if not root:
        return 

      # leaf node
      if not root.left and not root.right:
        if root.val <= target and len(small) < k:
          small.append(root.val)
        elif root.val >= target and len(big) < k:
          big.append(root.val)

        return 

      # if the small array is fully filled
      if high <= target and len(small) >= k:
        return

      # if the bigger array is fully filled
      if low >= target and len(big) >= k:
        return

      if root.val <= target:
        # search the right branch, which can fill either 
        # small or big arr
        search(root.right, root.val, high)

        # if we need more smaller ones
        if len(small) < k:
          small.append(root.val)
          search(root.left, low, root.val)

      else:
        # search the left branch, which may fill the small
        # or the big arr
        search(root.left, low, root.val)
        
        if len(big) < k:
          big.append(root.val)
          search(root.right, root.val, high)

      return

    # run the search
    search(root, -inf, inf)
    # small.sort(reverse=True)
    # big.sort()

    # sort the results
    print(small, big)
    ans = []
    i, j = 0, 0

    # create the answers by comparing which one is closer -- the next
    # smaller one or next bigger one
    while (len(ans) < k) and (i < len(small) or j < len(big)):
      if i >= len(small):
        ans.append(big[j])
        j += 1
        continue

      if j >= len(big):
        ans.append(small[i])
        i += 1
        continue

      if target-small[i] <= big[j]-target:
        ans.append(small[i])
        i += 1

      else:
        ans.append(big[j])
        j += 1

    return ans


s = Solution()
t = [
  [[4,2,5,1,3], 3.714286, 2, [4, 3]]
]

for tree, target, k, ans in t:
  res = s.closest_value(Solution.build_tree(tree), target, k)
  print('\n========\nTest case', tree, target, k)
  print('Expected:', ans)
  print('Gotten  :', res)
