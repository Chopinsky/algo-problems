'''
2458. Height of Binary Tree After Subtree Removal Queries

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.

Example 1:

Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).

Example 2:

Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).

Constraints:

The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
m == queries.length
1 <= m <= min(n, 10^4)
1 <= queries[i] <= n
queries[i] != root.val
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
  def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
    stack = [(root, 0)]
    below = {}
    above = {}
    levels = defaultdict(list)
    
    def update(node):
      val = node.val
      lvl = len(stack)
      above[val] = lvl
      below[val] = 0
      
      if node.left:
        below[val] = max(below[val], 1+below[node.left.val])
        
      if node.right:
        below[val] = max(below[val], 1+below[node.right.val])
      
      heappush(levels[lvl], (-below[val], val))
      
    while stack:
      node, step = stack.pop()
      if not node:
        continue
        
      if step == 2:
        update(node)
        continue
        
      if step == 1:
        stack.append((node, 2))
        stack.append((node.right, 0))
        continue
        
      stack.append((node, 1))
      stack.append((node.left, 0))
        
    # print('init:', below, above, levels)
    ans = []
    
    #todo
    max_level = max(levels)
    
    for q in queries:
      lvl = above[q]
      curr_lvl = levels[lvl]
      
      # not affecting the longest path
      if q != curr_lvl[0][1]:
        ans.append(max_level)
        continue
      
      # sole path, everything below is gone
      if len(curr_lvl) == 1:
        ans.append(lvl-1)
        continue
        
      # print('iter:', q, lvl, curr_lvl)
      side_long = -curr_lvl[1][0]
      if len(curr_lvl) > 2:
        side_long = max(side_long, -curr_lvl[2][0])
        
      ans.append(lvl+side_long)
    
    return ans
        
  def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
    depth = {}
    below = {}
    levels = defaultdict(list)
    
    def walk(root, d):
      if not root:
        return 0
      
      # the current depth from top-down
      depth[root.val] = d
      down = max(walk(root.left, d+1), walk(root.right, d+1))
      
      # get the max-depth below this node
      below[root.val] = down
      levels[d].append(down)
      
      # shift the value to a proper position -- bubble sort with array length <= 3 
      idx = len(levels[d])-1
      while idx > 0 and levels[d][idx] > levels[d][idx-1]:
        levels[d][idx], levels[d][idx-1] = levels[d][idx-1], levels[d][idx]
        idx -= 1

      # only care about 2 elements
      while len(levels[d]) > 2:
        levels[d].pop()

      # if len(levels[d]) > 1:
      #   levels[d] = sorted(levels[d], reverse=True)[:2]
        
      return down+1
      
    tree_depth = walk(root, 0) - 1
    ans = []
    # print(depth, levels, total)
    
    for q in queries:
      l = depth[q]
      b = below[q]
      # print(q, l, b, levels[l])
      
      if len(levels[l]) == 1:
        ans.append(l-1)
        
      else:
        if b == levels[l][0]:
          # take the next-greatest depth as the alt-tree-depth
          ans.append(l + levels[l][1])
          
        else:
          # not affecting depth
          ans.append(tree_depth)
          
    return ans
    