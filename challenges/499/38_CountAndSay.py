from functools import lru_cache


class Solution:
  @lru_cache(None)
  def say(val: str) -> str:
    res = ''
    last = val[0]
    count = 1
    
    for ch in val[1:]:
      if ch == last:
        count += 1
        
      else:
        if last and count > 0:
          # print('append:', last, count)
          res += str(count) + last
          
        last = ch
        count = 1
      
    if last and count > 0:
      # print('final append:', last, count)
      res += str(count) + last
      
    return res


  def countAndSay(self, n: int) -> str:
    base = '1'
    idx = 1

    while idx < n:
      base = self.say(base)
      idx += 1
      # print(i, base)
      
    return base
    