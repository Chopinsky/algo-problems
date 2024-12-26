'''
3331. Find Subtree Sizes After Changes
'''

from typing import List
from collections import defaultdict


class Solution:
  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    stacks = defaultdict(list)
    n = len(parent)
    
    def build_children(pt: List[int]):
      children = defaultdict(list)
      for i, p in enumerate(pt):
        if p < 0:
          continue

        children[p].append(i)
        
      return children
      
    children = build_children(parent)

    def traverse(u: int):
      if u >= n:
        return
      
      ch = s[u]
      stacks[ch].append(u)
      
      for v in children[u]:
        traverse(v)
        
      stacks[ch].pop()
      if stacks[ch]:
        parent[u] = stacks[ch][-1]
    
    def count(u: int, children, ans: List[int]):
      if u >= n:
        return 0
      
      c = 1
      for v in children[u]:
        c += count(v, children, ans)
        
      ans[u] = c
      
      return c
    
    traverse(0)
    ans = [0]*n
    count(0, build_children(parent), ans)
    
    return ans
  