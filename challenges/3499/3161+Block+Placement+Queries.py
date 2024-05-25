'''
3161. Block Placement Queries

There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

Example 1:

Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

Output: [false,true,true]

Explanation:


For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:

Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
Output: [true,true,false]

Explanation:

Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.

Constraints:

1 <= queries.length <= 15 * 10^4
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 10^4, 3 * queries.length)
The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
The input is generated such that there is at least one query of type 2.

Test cases:

[[1,4],[2,1,2]]
[[1,2],[2,3,3],[2,3,1],[2,2,2]]
[[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
'''

from typing import List

class Node:
  def __init__(self, l=0, r=0):
    self.l = l
    self.r = r
    self.sz = r-l
    self.o = None   # will be [first_obstacle_pos, last_obstacle_pos]
    self.lc = None
    self.rc = None
    
  def __repr__(self):
    return 'Node(l=' + str(self.l) + ',r=' + str(self.r) + ',sz=' + str(self.sz) + ',o=' + (str(self.o) if self.o else 'None') + ',lc=' + str(self.lc is not None) + ',rc=' + str(self.rc is not None) + ')'
    

class Solution:
  '''
  the idea is to use the range query on a segment-tree: there will be at most 10**5 nodes in this tree, making
  it log(n) time to update or query a result
  '''
  def getResults(self, queries: List[List[int]]) -> List[bool]:
    top = max(3, max(q[1] for q in queries))
    root = Node(l=0, r=top)
    # print('top:', top, root)
    
    def update(node: Node):
      mid = (node.l + node.r) // 2
      
      if not node.lc:
        lb = node.l
        lsz = mid - lb
      else:
        lb = node.lc.o[1]
        lsz = node.lc.sz
        
      if not node.rc:
        rb = node.r
        rsz = rb - mid
      else:
        rb = node.rc.o[0]
        rsz = node.rc.sz
        
      node.sz = max(rb-lb, lsz, rsz)
      if node.l == 0 and node.o:
        node.sz = max(node.sz, node.o[0])
      
      if node.r == top and node.o:
        node.sz = max(node.sz, node.r - node.o[1])
    
    def insert(node: Node, x: int):
      if not node:
        return
      
      if not node.o:
        node.o = [x, x]
      else:
        node.o[0] = min(node.o[0], x)
        node.o[1] = max(node.o[1], x)
        
      # this is the leaf node
      if node.l+1 >= node.r:
        update(node)
        return
        
      mid = (node.l + node.r) // 2
      
      if x < mid:
        # goes to the left node
        if not node.lc:
          node.lc = Node(l=node.l, r=mid)
          
        child = node.lc
        
      else:
        # goes to the right node
        if not node.rc:
          node.rc = Node(l=mid, r=node.r)
          
        child = node.rc
        
      insert(child, x)
      update(node)
    
    def query(node: Node, x: int):
      if not node:
        return 0
      
      if x >= node.r:
        return node.sz
      
      if not node.o:
        return x - node.l
        
      size = max(0, x-node.o[1])
      mid = (node.l + node.r) // 2
      s0 = query(node.lc, x)

      # goes to the left node
      if x < mid:
        s1 = min(x, node.o[0])-node.l
        # if node.l == 0 and node.r == 4:
        #   print('q0:', node.o, size, s0, s1)
          
        return max(size, s0, s1)
      
      # goes to both the left and the right node
      s1 = query(node.rc, x)
      lb = node.lc.o[1] if node.lc and node.lc.o else node.l
      rb = node.rc.o[0] if node.rc and node.rc.o else node.r
      s2 = max(0, min(x, rb)-lb)
      
      # if node.l == 0 and node.r == 4:
      #   print('q0:', size, s0, s1, s2)
        
      return max(size, s0, s1, s2)
    
    ans = []
    for q in queries:
      if q[0] == 1:
        # print('insert:', q[1])
        insert(root, q[1])
        continue
        
      max_size = query(root, q[1])
      # print('res:', (q[1], q[2]), max_size)
      ans.append(max_size >= q[2])
    
    return ans
    