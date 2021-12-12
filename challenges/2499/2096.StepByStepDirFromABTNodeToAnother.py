'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:

Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:

The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    if not root or startValue == destValue:
      return ''
    
    stack = [(root, 0, '')]
    trace0 = None
    trace1 = None
    
    while stack and (not trace0 or not trace1):
      node, state, dr = stack[-1]
      if not node:
        stack.pop()
        continue
      
      if node.val == startValue:
        trace0 = stack.copy()
      elif node.val == destValue:
        trace1 = stack.copy()
        
      if state >= 2:
        stack.pop()
        continue
        
      stack[-1] = (node, state+1, dr)
      stack.append((node.left if not state else node.right, 0, 'L' if not state else 'R'))
      
    lcp = 0
    while lcp+1 < len(trace0) and lcp+1 < len(trace1):
      if trace0[lcp+1][0].val != trace1[lcp+1][0].val:
        break
        
      lcp += 1
      
    path = 'U' * (len(trace0) - lcp - 1) + ''.join(node[2] for node in trace1[lcp+1:])
    
    '''
    print(lcp)
    for node, _, dr in trace0[lcp:]:
      print('0', node.val, dr)
    
    for node, _, dr in trace1[lcp:]:
      print('1', node.val, dr)
    '''
    
    return path
  