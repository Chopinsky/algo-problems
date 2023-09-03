from typing import List
from collections import defaultdict


class Solution:
  '''
  this problem requies 3 steps:
  1) build the euler path using dfs, store the weight frequencies from root to node u, and also the height
     of node u in the tree rooted at `root`;
  2) build the segment tree for the euler path from step 1, the value of this seg_tree is the lca of all
     the nodes in the range [begin, end] of the euler path, i.e., lca of euler_path[begin:end+1]
  3) for the queries, find the euler path that contains the first occurance of both u, v, then query the
     segment tree to pull the common ancestor node `lca`, then the number of weights in the path will be:
        weight_count = freq[u][w] + freq[v][w] - 2*freq[lca][w] for w in all possible weights
  '''
  def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    e = [[] for _ in range(n)]
    p = [-1] * n
    weights = set()
    
    '''
    part 1: build the weight frequence -> freq[u][w] is the number of edges with weight `w` in the path
    from `root` to node `u`; in this process, we will also build the euler path, the height of node `u`
    in the tree with `root` node, and the first occurance of the node `u` in the euler path
    '''
    start = 0
    freq = [None] * n
    freq[start] = defaultdict(int)
    
    path = []
    height = [0] * n
    first = [-1] * n

    for u, v, w in edges:
      e[u].append((v, w))
      e[v].append((u, w))
      weights.add(w)
      
    def dfs(u: int, h: int):
      path.append(u)
      height[u] = h
      first[u] = len(path)-1
      
      for v, w in e[u]:
        if v == p[u]:
          continue
          
        p[v] = u
        freq[v] = freq[u].copy()
        freq[v][w] += 1
        
        dfs(v, h+1)
        path.append(u)
    
    dfs(start, 0)
    # print(p, freq)
    # print(path, height, first)

    '''
    part 2: build the segment tree that stores the lowest common ancestor node for range [b, e] in 
    the euler path; e.g., for the subarray of the euler path [4, 2, 5, 2, 1, 3, 6] from example 2, the
    lca is node 1 since it has the lowest tree height; also query the segment tree using this algo
    '''
    # for [node] of the segment tree, which track the euler path
    # subarray in the range of [b, e]
    def build(v0: int, b: int, e: int):
      if b >= e:
        if b == e:
          seg_tree[v0] = path[b]
          
        return
      
      mid = (b + e) // 2
      left_node = v0 << 1
      right_node = left_node | 1
      
      build(left_node, b, mid)
      build(right_node, mid+1, e)
      
      vl = seg_tree[left_node]
      vr = seg_tree[right_node]
      
      seg_tree[v0] = vl if (height[vl] <= height[vr]) else vr
    
    # query the lca from the seg_tree @ node v0, with the range of [b, e]
    # coverage, for euler path of the subarray in the range of [l, r]
    def query(v0: int, b: int, e: int, l: int, r: int):
      if b > r or e < l:
        return -1
      
      if b >= l and e <= r:
        return seg_tree[v0]
      
      mid = (b + e) // 2
      left_node = v0 << 1
      right_node = left_node | 1
      
      vl = query(left_node, b, mid, l, r)
      vr = query(right_node, mid+1, e, l, r)
      
      if vl < 0:
        return vr
      
      if vr < 0:
        return vl
      
      return vl if height[vl] <= height[vr] else vr
      
    m = len(path)
    seg_tree = [-1] * (4*m)
    build(1, 0, m-1)
    # print('seg tree:', seg_tree)
    
    '''
    part 3: for each query, find the range in euler path which contains the first occurance of `u`, `v`, 
    respectively, then query the seg_tree for the lca of this euler path range, which will be the lca 
    for `u` and `v`.
    '''
    ans = []
    for u, v in queries:
      left = first[u]
      right = first[v]
      
      if right < left:
        left, right = right, left
        
      # print('q:', (u, v), (left, right), path[left:right+1])
      lca = query(1, 0, m-1, left, right)
      total = 0
      top = 0
      
      for w in weights:
        w0 = freq[u][w] + freq[v][w] - 2*freq[lca][w]
        total += w0
        top = max(top, w0)
        
      # print('res:', (u, v), '->', lca, (total, top))
      ans.append(total-top)
    
    return ans
  