'''
1261-find-elements-in-a-contaminated-binary-tree
'''


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class FindElements:
  def __init__(self, root: Optional[TreeNode]):
    self.vals = set()
    def dfs(node, val: int):
      if not node:
        return

      node.val = val
      self.vals.add(val)

      if node.left:
        dfs(node.left, 2*val+1)

      if node.right:
        dfs(node.right, 2*val+2)

    dfs(root, 0)
    # print('init:', self.vals)

  def find(self, target: int) -> bool:
    return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)