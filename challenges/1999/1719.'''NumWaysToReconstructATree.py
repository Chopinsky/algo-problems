'''
You are given an array pairs, where pairs[i] = [xi, yi], and:

There are no duplicates.
xi < yi
Let ways be the number of rooted trees that satisfy the following conditions:

The tree consists of nodes whose values appeared in pairs.
A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.
Note: the tree does not have to be a binary tree.
Two ways are considered to be different if there is at least one node that has different parents in both ways.

Return:

0 if ways == 0
1 if ways == 1
2 if ways > 1
A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.

Example 1:


Input: pairs = [[1,2],[2,3]]
Output: 1
Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
Example 2:


Input: pairs = [[1,2],[2,3],[1,3]]
Output: 2
Explanation: There are multiple valid rooted trees. Three of them are shown in the above figures.
Example 3:

Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
Output: 0
Explanation: There are no valid rooted trees.
 

Constraints:

1 <= pairs.length <= 10^5
1 <= xi < yi <= 500
The elements in pairs are unique.
'''


from typing import List, Tuple
from collections import defaultdict


class Solution:
  def checkWays(self, pairs: List[List[int]]) -> int:
    if len(pairs) == 1:
      return 2
      
    e = defaultdict(set)
    for u, v in pairs:
      e[u].add(v)
      e[v].add(u)
      
    tree = {}
    total = len(e)
    checked = set()
    root_node = -1
    
    for u in e:
      if u not in tree:
        tree[u] = [0, set(), set()]
          
      for v in e[u]:
        key = (min(u, v), max(u, v))
        if key in checked:
          continue
          
        checked.add(key)
        
        if v not in tree:
          tree[v] = [0, set(), set()]
          
        if len(e[u]) > len(e[v]):
          # u is the parent of v with branches
          tree[v][0] += 1
          tree[u][2].add(v)
        elif len(e[u]) < len(e[v]):
          # u is the chidlren of u
          tree[u][0] += 1
          tree[v][2].add(u)
        else:
          tree[u][1].add(v)
          tree[v][1].add(u)
      
      if not tree[u][0] and len(tree[u][2]) + len(tree[u][1]) == total-1:
        root_node = u
    
    if root_node < 0:
      return 0
    
    checked = set()
    # print('init', tree, root_node)
    
    def check_tree(u: int) -> Tuple[int, int]:
      nonlocal checked
        
      checked.add(u)
      checked |= tree[u][1]
      has_chain = len(tree[u][1]) > 0

      # subtree cross with examined nodes
      if tree[u][2] & checked:
        # print('fail 0', u, tree[u][2] & checked, checked)
        return (0, 0)

      # subtree does not match with a peer, which shall be in the 
      # sole-chain and need to match with `u`'s subtree
      for v in tree[u][1]:
        if tree[u][2] != tree[v][2]:
          # print('fail 1')
          return (0, 0)

      # check all subtree nodes
      subtree_cnt = 0
      for v in sorted(tree[u][2], key=lambda x: -len(tree[x][2])):
        if v in checked:
          continue
          
        ways, cnt = check_tree(v)
        subtree_cnt += cnt

        if not ways:
          # print('fail 2')
          return (0, 0)

        if ways == 2:
          has_chain = True

      # if we have more nodes from the subtree than allowed (i.e. from
      # the current tree), this is invalid
      if subtree_cnt != len(tree[u][2]):
        # print('fail 3')
        return (0, 0)
        
      # if we have a chain at this level or at a subtree level, we will 
      # have more than 1 way to construct this segment of the tree
      return (2 if has_chain else 1, 1+len(tree[u][1])+subtree_cnt)
      
    ways, _ = check_tree(root_node)
    return ways
  

  def checkWays0(self, pairs: List[List[int]]) -> int:
    graph = defaultdict(set)
    seen = set()
    
    for u, v in pairs:
      graph[u].add(v)
      graph[v].add(u)

    def check(root: int) -> Tuple[int, int]:
      seen.add(root)
      children = sorted([(len(graph[v]), v) for v in graph[root]], reverse=True)
      n = len(graph[root])
      
      node_count = 1
      ways = 1
      
      # remove root since it's the parent
      for _, v in children:
        if len(graph[v]) == n:
          # this node is in a chain with the root, we can rearrange them
          # to get more than 1 valid tree (aka a trunk-chain)
          ways = 2
          node_count += 1
          seen.add(v)
          
        # remove the root from this node, since we go down and shouldn't
        # ever go up the tree
        graph[v].remove(root)

      # now let's try all children
      for _, v in children:
        # if v is a branch in another subtree, or a peer (i.e. in the same
        # chain with the root), skip
        if v in seen:
          continue
          
        # now v is the root of a subtree, begin recursion
        subtree_ways, subtree_nodes = check(v)
        node_count += subtree_nodes
        
        # no way to construct a subtree from root-v
        if subtree_ways == 0:
          return (0, 0)
        
        # more than 1 way to construct the subtree, this
        # tree will have more than 1 way to construct as well
        if subtree_ways == 2:
          ways = 2
              
      # more nodes than allowed -- root must contain all subtree nodes,
      # but not more
      if node_count > n + 1:
        return (0, 0)
          
      return ways, node_count
    
    total = len(graph)
    for u in graph:
      # this can be a root
      if len(graph[u]) == total - 1:
        ways, _ = check(u)
        return ways
      
    return 0
    