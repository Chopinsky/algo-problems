'''
2385. Amount of Time for Binary Tree to Be Infected

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

Example 1:
https://assets.leetcode.com/uploads/2022/06/25/image-20220625231744-1.png

Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:
https://assets.leetcode.com/uploads/2022/06/25/image-20220625231812-2.png

Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
Each node has a unique value.
A node with a value of start exists in the tree.
'''

from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    e = defaultdict(list)
    
    def conn(root):
      if not root:
        return
      
      val = root.val
      if root.left:
        lval = root.left.val
        e[val].append(lval)
        e[lval].append(val)
        conn(root.left)
        
      if root.right:
        rval = root.right.val
        e[rval].append(val)
        e[val].append(rval)
        conn(root.right)
      
    conn(root)
    # print(e)
    
    curr, nxt = [start], []
    seen = set(curr)
    time = 0
    
    while curr:
      for u in curr:
        for v in e[u]:
          if v in seen:
            continue
            
          nxt.append(v)
          seen.add(v)
      
      curr, nxt = nxt, curr
      nxt.clear()
      
      if curr:
        time += 1
    
    return time
  

  def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    graph = defaultdict(list)
    infected = set()
    
    def build_graph(root):
      rv = root.val
      if root.left:
        left = root.left.val  
        graph[rv].append(left)
        graph[left].append(rv)
        build_graph(root.left)
        
      if root.right:
        right = root.right.val
        graph[rv].append(right)
        graph[right].append(rv)
        build_graph(root.right)
    
    def dfs(u: int) -> int:
      # print('visit:', u)
      infected.add(u)
      time = 0
      
      for v in graph[u]:
        if v in infected:
          continue
          
        time = max(time, 1 + dfs(v))
        
      return time
        
    build_graph(root)
    # print(graph)
    
    return dfs(start)
