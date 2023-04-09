"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""


from collections import deque


# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    seen = {}
    
    def copy(root):
      if not root:
        return None
      
      v0 = root.val
      if v0 in seen:
        return seen[v0]
      
      curr = Node(v0)
      seen[v0] = curr
      
      for node in root.neighbors:
        v1 = node.val
        if v1 not in seen:
          nn = copy(node)
        else:
          nn = seen[v1]
          
        if nn:
          curr.neighbors.append(nn)
      
      return curr
      
    return copy(node)
  

  def cloneGraph(self, node: 'Node') -> 'Node':
    nodes = {}
    
    def clone(curr: 'Node') -> 'Node':
      if curr is None:
        return None

      if curr in nodes:
        return nodes[curr]

      nodes[curr] = Node(curr.val)
      for adj in curr.neighbors:
        nodes[curr].neighbors.append(clone(adj))

      return nodes[curr]

    return clone(node)
      
      
  def cloneGraph0(self, node: 'Node') -> 'Node':
    if not node:
      return None
    
    root = None
    edges = set()
    
    nodes = {}
    stack = deque([node])
    
    while stack:
      curr = stack.popleft()
      
      # the node has already been visited
      if curr.val in nodes:
        continue

      copy = Node(curr.val)
      nodes[curr.val] = copy
      
      if not root:
        root = copy
      
      for nxt in curr.neighbors:
        edges.add((min(curr.val, nxt.val), max(curr.val, nxt.val)))
        if nxt.val in nodes or nxt.val in stack:
          continue
          
        stack.append(nxt)
      
    for a, b in edges:
      na, nb = nodes[a], nodes[b]
      if na.neighbors is None:
        na.neighbors = []
        
      if nb.neighbors is None:
        nb.neighbors = []
        
      na.neighbors.append(nb)
      nb.neighbors.append(na)
    
    return root
  