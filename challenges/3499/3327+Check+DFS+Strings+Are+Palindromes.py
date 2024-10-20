'''
3327. Check if DFS Strings Are Palindromes
'''

from collections import defaultdict
from typing import List


class Solution:
  '''
  the key is to use Manacher's algorithm to compute the parlindrom length centered
  at every possible position of the resulting string, aka `dfsStr`. `dfsStr` can 
  be easily built from running the `dfs` as described from the problem, and each 
  subtree will be a substring in the `dfsStr`, we just need to check if the subtree's
  substring is a palindrom (aka `pal_len[subtree_idx] >= subtree_size`)
  '''
  def findAnswer(self, parent: List[int], s: str) -> List[bool]:
    tree = defaultdict(list)
    for v, u in enumerate(parent):
      if v == 0:
        continue
        
      tree[u].append(v)
      
    nodes = {}
    src = ""
    
    def build(u: int):
      nonlocal src 
      
      l = len(src)
      if u not in tree:
        src += s[u]
        nodes[u] = [l, l]
        return
      
      for v in tree[u]:
        build(v)
        
      src += s[u]
      r = len(src)-1
      nodes[u] = [l, r]
      
    build(0)
    ln = len(parent)
    ans = []
    # print('init:', tree, src, nodes)
    
    def manachers_odd(s: str) -> List:
      n = len(s)
      p = [0]*(n+2)
      s = "$" + s + "^"
      l, r = 1, 1
      # print('updated:', s)
      
      for i in range(1, n+1):
        p[i] = max(0, min(r-i, p[l+(r-i)]))
        while s[i-p[i]] == s[i+p[i]]:
          p[i] += 1
          
        if i+p[i] > r:
          l = i-p[i]
          r = i+p[i]
      
      return p[1:-1]
      
    def manachers(s: str) -> List:
      updated = ["#"+ch for ch in s] + ["#"]
      long = manachers_odd("".join(updated))
      
      for i in range(len(long)):
        side = (long[i]-1) // 2
        long[i] = 2*side + (1 if i%2 == 1 else 0)
        
      return long
    
    pal_len = manachers(src)
    # print('pal_len:', pal_len)
    
    def check(ln: List, u: int) -> bool:
      l, r = nodes[u]
      ln = (r-l+1)
      mid = (l+r) // 2
      
      idx = 2*mid+1
      if ln%2 == 0:
        idx += 1
      
      return pal_len[idx] >= ln
    
    for u in range(ln):
      ans.append(check(pal_len, u))
    
    return ans
    