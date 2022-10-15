'''
2440. Create Components With Same Value

There is an undirected tree with n nodes labeled from 0 to n - 1.

You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are allowed to delete some edges, splitting the tree into multiple connected components. Let the value of a component be the sum of all nums[i] for which node i is in the component.

Return the maximum number of edges you can delete, such that every connected component in the tree has the same value.

Example 1:

Input: nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]] 
Output: 2 
Explanation: The above figure shows how we can delete the edges [0,1] and [3,4]. The created components are nodes [0], [1,2,3] and [4]. The sum of the values in each component equals 6. It can be proven that no better deletion exists, so the answer is 2.
Example 2:

Input: nums = [2], edges = []
Output: 0
Explanation: There are no edges to be deleted.

Constraints:

1 <= n <= 2 * 10^4
nums.length == n
1 <= nums[i] <= 50
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
edges represents a valid tree.
'''

from typing import List
from collections import defaultdict, Counter


class Solution:
  def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
    if not edges:
      return 0
    
    n = len(nums)
    if len(set(nums)) == 1:
      return n-1
    
    e = defaultdict(set)
    total = sum(nums)
    leaf = set(i for i in range(n))
    
    for u, v in edges:
      e[u].add(v)
      e[v].add(u)
      
      if len(e[u]) > 1:
        leaf.discard(u)
        
      if len(e[v]) > 1:
        leaf.discard(v)

    parent = [-1] * n
    degrees = [0] * n
    curr, nxt = list(leaf), []
    seen = set()
    
    while len(curr) >= 2:
      # tree with dual roots
      if len(curr) == 2 and len(seen)+2 == n:
        break
        
      for u in curr:
        if u in seen or not e[u]:
          continue
          
        seen.add(u)
        p = e[u].pop()
        e[p].discard(u)
        
        parent[u] = p
        degrees[p] += 1
        
        if len(e[p]) == 1:
          nxt.append(p)
          
      curr, nxt = nxt, curr
      nxt.clear()
    
    # print(parent)
    
    def can_form(c: int) -> bool:
      target = total // c
      subtree = nums.copy()
      d = degrees.copy()
      cand, nxt = list(leaf), []
      comp_cnt = 0
      seen = set()
      # print('test:', total, c, target)
      
      while cand:
        # print('iter:', cand, comp_cnt)
        if len(cand) == 2 and len(seen)+2 == n:
          a, b = cand[0], cand[1]
          
          if subtree[a] == subtree[b] == target:
            comp_cnt += 2
          elif subtree[a] + subtree[b] == target:
            comp_cnt += 1
          else:
            if subtree[a] == target:
              comp_cnt += 1
              
            if subtree[b] == target:
              comp_cnt += 1
              
          break
          
        for u in cand:
          seen.add(u)
          
          # invalid case
          if subtree[u] > target:
            return False
          
          # formed a subtree component, update counter
          if subtree[u] == target:
            comp_cnt += 1

          p = parent[u]
          if p >= 0:
            d[p] -= 1

            # smaller, add to the parent
            if subtree[u] < target:
              subtree[p] += subtree[u]

            # all children components have been seen
            if d[p] == 0:
              nxt.append(p)
        
        cand, nxt = nxt, cand
        nxt.clear()
      
      return comp_cnt == c
    
    for c in range(total//min(nums), 1, -1):
      if total % c != 0:
        continue
        
      if can_form(c):
        return c-1
      
    return 0


  def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
    if not edges:
      return 0
    
    n = len(nums)
    # print(set(nums))

    if len(set(nums)) == 1:
      return n-1
    
    e = defaultdict(set)
    leaf = set(i for i in range(n))
    
    # build the tree
    for u, v in edges:
      e[u].add(v)
      e[v].add(u)
      
      if len(e[u]) > 1:
        leaf.discard(u)
        
      if len(e[v]) > 1:
        leaf.discard(v)

    subtree = nums.copy()
    stack, nxt = list(leaf), list()
    seen = set()
    parent = [-1] * n
    
    # build the tree direction: from leaf to parent
    while len(stack) >= 2:
      if len(stack) == 2 and len(seen)+2 == n:
        break
        
      # print('stack:', stack)
      for u in stack:
        if u in seen:
          continue

        seen.add(u)
        v = e[u].pop()
        parent[u] = v
        
        subtree[v] += subtree[u]
        e[v].discard(u)

        if len(e[v]) == 1:
          nxt.append(v)
          
      stack, nxt = nxt, stack
      nxt.clear()
    
    counter = Counter(subtree)
    total = sum(nums)
    # print([i for i in range(n) if parent[i] == -1])
    # print('subtree:', subtree)
    
    def can_cut(count: int) -> bool:
      comp_sum = total // count
      # print(count, '->', comp_sum, counter.get(comp_sum, -1), counter)
      
      if comp_sum not in counter:
        return False
    
      if counter[comp_sum] == count-1 or counter[comp_sum] == count:
        return True
      
      #todo: bsf try reduce
      cand, nxt = [i for i in range(n) if subtree[i] == comp_sum], []
      comp_cnt = 0
      ss = subtree.copy()
      seen = set()
      
      while cand:
        comp_cnt += len(cand)
        
        for u in cand:
          if u in seen:
            continue
            
          seen.add(u)
          v = parent[u]
          
          ss[v] -= subtree[u]
          if ss[v] == comp_sum:
            nxt.append(v)
        
        # print('bfs iter:', len(cand), len(nxt), comp_cnt)
        cand, nxt = nxt, cand
        nxt.clear()
      
      return comp_cnt == n

    start = total // min(nums)
    # end = max(1, total//max(nums[i] for i in leaf)-1)
    # print('overall:', total, start, end)
    
    for i in range(start, 1, -1):
      if total % i != 0:
        continue
      
      if can_cut(i):
        return i-1
      
    return 0
  