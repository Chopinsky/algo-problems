'''
3335. Total Characters in String After Transformations I
'''

class Solution:
  def lengthAfterTransformations(self, s: str, t: int) -> int:
    mod = 10**9+7
    curr = [0]*26
    for ch in s:
      curr[ord(ch)-ord('a')] += 1
    
    def transform(curr):
      nxt = [0]*26
      
      for idx, cnt in enumerate(curr):
        if idx == 25:
          nxt[0] = (nxt[0] + cnt) % mod
          nxt[1] = (nxt[1] + cnt) % mod
        else:
          nxt_ch = idx+1
          nxt[nxt_ch] = (nxt[nxt_ch] + cnt) % mod
      
      return nxt
    
    while t > 0:
      curr = transform(curr)
      t -= 1
      
    return sum(curr) % mod
  