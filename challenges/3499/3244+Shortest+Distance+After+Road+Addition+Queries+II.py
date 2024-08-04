'''
3244. Shortest Distance After Road Addition Queries II

You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

There are no two queries such that queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1].

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

Example 1:

Input: n = 5, queries = [[2,4],[0,2],[0,4]]

Output: [3,2,1]

Explanation:

After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.

After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.

After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

Example 2:

Input: n = 4, queries = [[0,3],[0,2]]

Output: [1,1]

Explanation:

After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.

After the addition of the road from 0 to 2, the length of the shortest path remains 1.

Constraints:

3 <= n <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
There are no repeated roads among the queries.
There are no two queries such that i != j and queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]

Test cases:

5
[[2,4],[0,2],[0,4]]
4
[[0,3],[0,2]]
6
[[1,5],[3,5]]
'''

from typing import List

class Node:
  def __init__(self, l, r, m=0):
    self.l = l
    self.r = r
    self.m = m
    self.lc = None
    self.rc = None
  

class Solution:
  '''
  this is a range query problem: use the range query tree to store the nodes that's been
  marked by each query: [l+1, r-1] (if l+1 > r-1, just skip, as it does not provide new
  information to the count); then the root node stores the number of nodes been marked
  after the query, and the steps equals `total_node - marked_node - 1`, as the last node
  will not count into the final step
  '''
  def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    root = Node(0, n-1)
    ans = []
    
    def mark(node, l: int, r: int):
      # no jump
      if l > r:
        return
      
      # no interception
      if l > node.r or r < node.l:
        return
      
      # already marked
      if node.m == node.r-node.l+1:
        return
      
      # entirely marked
      if l <= node.l and node.r <= r:
        node.m = node.r-node.l+1
        return
      
      mid = (node.l + node.r) // 2
      if not node.lc:
        node.lc = Node(node.l, mid)
        
      if not node.rc:
        node.rc = Node(mid+1, node.r)
        
      mark(node.lc, l, r)
      mark(node.rc, l, r)
      
      node.m = node.lc.m + node.rc.m
      # print('done:', node.l, node.r, node.m)
    
    def show(node):
      print('c:', (node.l, node.r), node.m)
      if node.lc:
        show(node.lc)
      if node.rc:
        show(node.rc)
    
    def count(node) -> int:
      # show(node)
      return n - node.m - 1 
    
    for l, r in queries:
      # print('q:', (l, r))
      mark(root, l+1, r-1)
      ans.append(count(root))  
        
    return ans
  