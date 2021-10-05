'''
There is a rooted tree consisting of n nodes numbered 0 to n - 1. Each node's number denotes its unique genetic value (i.e. the genetic value of node x is x). The genetic difference between two genetic values is defined as the bitwise-XOR of their values. You are given the integer array parents, where parents[i] is the parent for node i. If node x is the root of the tree, then parents[x] == -1.

You are also given the array queries where queries[i] = [nodei, vali]. For each query i, find the maximum genetic difference between vali and pi, where pi is the genetic value of any node that is on the path between nodei and the root (including nodei and the root). More formally, you want to maximize vali XOR pi.

Return an array ans where ans[i] is the answer to the ith query.

Example 1:


Input: parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]
Output: [2,3,7]
Explanation: The queries are processed as follows:
- [0,2]: The node with the maximum genetic difference is 0, with a difference of 2 XOR 0 = 2.
- [3,2]: The node with the maximum genetic difference is 1, with a difference of 2 XOR 1 = 3.
- [2,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.

Example 2:

Input: parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]
Output: [6,14,7]
Explanation: The queries are processed as follows:
- [4,6]: The node with the maximum genetic difference is 0, with a difference of 6 XOR 0 = 6.
- [1,15]: The node with the maximum genetic difference is 1, with a difference of 15 XOR 1 = 14.
- [0,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.

Constraints:

2 <= parents.length <= 10 ^ 5
0 <= parents[i] <= parents.length - 1 for every node i that is not the root.
parents[root] == -1
1 <= queries.length <= 3 * 10 ^ 4
0 <= nodei <= parents.length - 1
0 <= vali <= 2 * 10 ^ 5
'''


from collections import defaultdict
from typing import List


class Trie:
  def __init__(self):
    self.root = [None, None, 0]
    
    
  def add(self, n: int):
    curr = self.root
    
    for i in range(18, -1, -1):
      bit = (n >> i) & 1
      if not curr[bit]:
        curr[bit] = [None, None, 0]
        
      curr = curr[bit]
      curr[2] += 1
      
      
  def remove(self, n: int):
    curr = self.root
    
    for i in range(18, -1, -1):
      bit = (n >> i) & 1
      curr[bit][2] -= 1
      curr = curr[bit]
      
      
  def max_xor(self, n: int) -> int:
    curr = self.root
    ans = 0
    
    for i in range(18, -1, -1):
      bit = (n >> i) & 1
      if curr[1^bit] and curr[1^bit][2] > 0:
        curr = curr[1^bit]
        ans |= 1 << i
      else:
        curr = curr[bit]
        
    return ans

  
class Solution:
  def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
    '''
    def walk(curr: int, val: int) -> int:
      base = curr^val
      while parents[curr] >= 0:
        curr = parents[curr]
        base = max(base, curr^val)
      return base
    ans = [walk(n, v) for n, v in queries]
    '''
    
    root = Trie()
    tree = defaultdict(list)
    q = defaultdict(list)
    root_node = None
  
    for i, p in enumerate(parents):
      if p < 0:
        root_node = i
      else:
        tree[p].append(i)
      
    for i, d in enumerate(queries):
      q[d[0]].append((d[1], i))
      
    # print(tree, q)
    
    ans = [0 for _ in range(len(queries))]
    stack = [root_node]
    root.add(root_node)
    
    while stack:
      # print(stack)
      
      # calc max-XOR for queries
      for val, i in q[stack[-1]]:
        ans[i] = root.max_xor(val)
      
      while stack and not tree[stack[-1]]:
        val = stack.pop()
        root.remove(val)
      
      if stack and tree[stack[-1]]:
        nxt = tree[stack[-1]].pop()
        stack.append(nxt)
        root.add(nxt)
    
    return ans
        