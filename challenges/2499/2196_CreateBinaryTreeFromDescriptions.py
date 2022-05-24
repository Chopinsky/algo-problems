'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

Example 1:

Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:

Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.

Constraints:

1 <= descriptions.length <= 10^4
descriptions[i].length == 3
1 <= parenti, childi <= 10^5
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    tree = {}
    p = set()
    c = set()
    
    for parent, val, left in descriptions:
      p.add(parent)
      c.add(val)
      
      if parent not in tree:
        tree[parent] = [0, 0]
        
      if left == 1:
        tree[parent][0] = val
      else:
        tree[parent][1] = val
        
    # print(tree, p, c, p-c)
    p -= c
    
    def build(curr):
      # print('build:', curr)
      root = TreeNode(curr)
      if curr in tree:
        l, r = tree[curr]

        if l > 0:
          root.left = build(l)

        if r > 0:
          root.right = build(r)

      return root
    
    return build(p.pop())
  