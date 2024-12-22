'''
3399. Smallest Substring With Identical Characters II

"000001"
1
"0000"
2
"0101"
0
"000000"
1
'''


class Solution:
  def minLength(self, s: str, ops: int) -> int:
    stack = []
    curr = s[0]
    cnt = 1
    long = 1
    n = len(s)
    
    for i in range(1, n):
      if s[i] == curr:
        cnt += 1
      else:
        stack.append(cnt)
        long = max(long, cnt)
        curr = s[i]
        cnt = 1
  
    stack.append(cnt)
    long = max(long, cnt)
    # print('init:', stack, long)
    
    if ops == 0 or long == 1:
      return long
    
    def count_ln_one():
      ch0, ch1 = '0', '1'
      ops0, ops1 = 0, 0
      
      for i in range(n):
        if s[i] != ch0:
          ops0 += 1
          
        if s[i] != ch1:
          ops1 += 1
          
        ch0 = '1' if ch0 == '0' else '0'
        ch1 = '1' if ch1 == '0' else '0'
      
      return min(ops0, ops1)
      
    def check(c0: int) -> bool:
      rem = ops
      
      for i in range(len(stack)):        
        c1 = stack[i]
        if c1 <= c0:
          continue
          
        rem -= c1 // (c0+1)
        if rem < 0:
          return False
      
      return rem >= 0
      
    # print('test 1:', count_ln_one())
    if count_ln_one() <= ops:
      return 1
      
    l, r = 2, n
    long = r
    
    while l <= r:
      mid = (l+r) // 2
      if check(mid):
        long = mid
        r = mid-1
      else:
        l = mid+1
    
    return long
        