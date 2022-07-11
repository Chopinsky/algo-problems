'''
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:

Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:

Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Constraints:

The number of nodes in the tree is in the range [1, 2^10].
1 <= Node.val <= 100
1 <= distance <= 10
'''

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def countPairs(self, root: TreeNode, distance: int) -> int:
    count = 0
    
    def test(root: TreeNode):
      nonlocal count
      
      if not root:
        return {}
      
      left = test(root.left)
      right = test(root.right)
      curr = defaultdict(int)
      # print(root.val, left, right)
      
      if not left and not right:
        curr[1] += 1
        return curr
      
      left_dist, right_dist = sorted(left), sorted(right)
      for d0 in left_dist:
        if d0 < distance:
          curr[d0+1] += left[d0]
        
        for d1 in right_dist:
          if d0 + d1 > distance:
            break
          
          # print('calc:', left[d0], right[d1])
          count += left[d0] * right[d1]
            
      for d1 in right_dist:
        if d1 >= distance:
          break
          
        curr[d1+1] += right[d1]
        
      return curr
    
    test(root)
    
    return count
    