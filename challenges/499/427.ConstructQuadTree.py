'''
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

Example 3:

Input: grid = [[1,1],[1,1]]
Output: [[1,1]]
Example 4:

Input: grid = [[0]]
Output: [[1,0]]
Example 5:

Input: grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
Output: [[0,1],[1,1],[1,0],[1,0],[1,1]]
 

Constraints:

n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6
'''

from typing import List


# Definition for a QuadTree node.
class Node:
  def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
    self.val = val
    self.isLeaf = isLeaf
    self.topLeft = topLeft
    self.topRight = topRight
    self.bottomLeft = bottomLeft
    self.bottomRight = bottomRight


class Solution:
  def construct(self, grid: List[List[int]]) -> 'Node':
    n = len(grid)
    
    def build(x: int, y: int, s: int) -> 'Node':
      val = grid[x][y]
      done = True
      
      for i in range(x, x+s):
        for j in range(y, y+s):
          if grid[i][j] != val:
            done = False
            break
            
        if not done:
          break
          
      if done:
        return Node(val, True, None, None, None, None)
      
      root = Node(val, False, None, None, None, None)
      s0 = s // 2
      
      root.topLeft = build(x, y, s0)
      root.topRight = build(x, y+s0, s0)
      root.bottomLeft = build(x+s0, y, s0)
      root.bottomRight = build(x+s0, y+s0, s0)
      
      return root
      
    return build(0, 0, n)
    

  def construct(self, grid: List[List[int]]) -> Node:
    n = len(grid)
    
    def build(x0: int, y0: int, x1: int, y1: int) -> Node:
      if x0 == x1:
        return Node(val=(grid[x0][y0] == 1), isLeaf=True)
        
      val = grid[x0][y0]
      root = Node(val=(val == 1))
      invalid = any(grid[i][j] != val for j in range(y0, y1+1) for i in range(x0, x1+1))
      
      if not invalid:
        root.isLeaf = True
        return root
      
      size = (x1-x0) // 2
      root.topLeft = build(x0, y0, x0+size, y0+size)
      root.topRight = build(x0, y0+size+1, x0+size, y1)
      root.bottomLeft = build(x0+size+1, y0, x1, y0+size)
      root.bottomRight = build(x0+size+1, y0+size+1, x1, y1)
      
      return root
      
    r = build(0, 0, n-1, n-1)
    # print(r.val, r.isLeaf)
    
    return r
  