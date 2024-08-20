'''
3015. Count the Number of Houses at a Certain Distance I
'''

from typing import List

class Solution:
  def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
    if x > y:
      x, y = y, x
      
    if y-x <= 1:
      cnt = 2*(n-1)
      ans = []
      
      while cnt >= 0:
        ans.append(cnt)
        cnt -= 2
      
      return ans
    
    ans = [0]*n
    
    def count(i: int) -> int:
      curr, nxt = [i], []
      seen = set(curr)
      d = 0
      
      while curr:
        d += 1
        c = 0
        # print('iter:', d, curr)
        
        for u in curr:
          if u-1 > 0 and u-1 not in seen:
            seen.add(u-1)
            nxt.append(u-1)
            c += 1
            
          if u+1 <= n and u+1 not in seen:
            seen.add(u+1)
            nxt.append(u+1)
            c += 1
            
          if u == x and y not in seen:
            seen.add(y)
            nxt.append(y)
            c += 1
            
          if u == y and x not in seen:
            seen.add(x)
            nxt.append(x)
            c += 1
            
        ans[d-1] += c
        curr, nxt = nxt, curr
        nxt.clear()
    
    for i in range(1, n+1):
      count(i)
      
    return ans
    