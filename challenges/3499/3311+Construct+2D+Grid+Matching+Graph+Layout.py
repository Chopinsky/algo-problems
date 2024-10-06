'''
3311. Construct 2D Grid Matching Graph Layout
'''

from typing import List
from collections import defaultdict

class Solution:
  def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    e = defaultdict(list)
    heads = []
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
      
    for u in e:
      if not heads or len(e[u]) == len(e[heads[0]]):
        heads.append(u)
      elif len(e[u]) < len(e[heads[0]]):
        heads.clear()
        heads.append(u)
        
    # print(e, heads)
    used = set()
    
    def build_top_row(heads: List[int], used):
      p = [-1]*n
      head = heads[0]
      target = set(heads[1:])
      curr, nxt = [head], []
      seen = set(curr)
      tail = head
      done = False
      
      while curr and not done:
        for u in curr:
          if done:
            break
            
          for v in e[u]:
            if v in seen:
              continue
            
            p[v] = u
            if v in target:
              done = True
              tail = v
              break
                          
            seen.add(v)
            nxt.append(v)
            
        curr, nxt = nxt, curr
        nxt.clear()
        
      row = []
      # print('tail:', tail)
      
      while tail != head:
        row.append(tail)
        tail = p[tail]
      
      row.append(head)
      used |= set(row)
      
      return row
    
    def build_nxt_row(prev: List[int], used, top, col):
      row = []
      prev_head = prev[0]
      
      for v in e[prev_head]:
        if v == top or (len(prev) > 1 and v == prev[1]):
          continue
          
        row.append(v)
        break
      
      for c in range(1, col_cnt):
        left = row[-1]
        top = prev[c]
        
        for v in e[left]:
          if v in used:
            continue
            
          if v in e[top]:
            row.append(v)
            break
      
      used |= set(row)
      
      return row
    
    ans = [build_top_row(heads, used)]
    col_cnt = len(ans[0])
    row_cnt = n // col_cnt
    
    for r in range(1, row_cnt):
      top = ans[-2][0] if r > 1 else -1
      ans.append(build_nxt_row(ans[-1], used, top, col_cnt))
      
    return ans
        