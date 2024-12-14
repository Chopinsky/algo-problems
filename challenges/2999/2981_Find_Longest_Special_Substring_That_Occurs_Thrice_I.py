'''
2981. Find Longest Special Substring That Occurs Thrice I
'''

from collections import Counter

class Solution:
  def maximumLength(self, s: str) -> int:
    c = Counter(s)
    if all(cnt < 3 for cnt in c.values()):
      return -1
    
    stack = []
    last = s[0]
    cnt = 1
    
    for ch in s[1:]+'$':
      if ch != last and cnt > 0:
        stack.append((last, cnt))
        last = ch
        cnt = 1
      else:
        cnt += 1
    
    # print('init:', stack)
    
    def check(ln: int) -> bool:
      c0 = defaultdict(int)
      
      for ch, cnt in stack:
        if cnt < ln:
          continue
          
        c0[ch] += cnt-ln+1
      
      return any(val >= 3 for val in c0.values())
    
    l, r = 1, len(s)
    last = 1
    
    while l <= r:
      mid = (l+r)//2
      if check(mid):
        last = mid
        l = mid+1
      else:
        r = mid-1
  
    return last
  