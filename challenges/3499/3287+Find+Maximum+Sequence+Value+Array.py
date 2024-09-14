'''
3287. Find the Maximum Sequence Value of Array
'''

from typing import List

class Solution:
  def maxValue(self, nums: List[int], k: int) -> int:
    curr, nxt = set([(0, 0)]), set()
    forward = []
    backward = []
    n = len(nums)
    
    def calc(i, curr, nxt):
      val = nums[i]
      seq = set()
      # print('iter:', i, curr)
      
      for base, ln in curr:
        base |= val
        if ln+1 == k:
          seq.add(base)
        else:
          nxt.add((base, ln+1))
        
      # forward.append(seq)
      nxt |= curr
      curr.clear()
      
      return seq, nxt, curr
    
    for i in range(n):
      seq, curr, nxt = calc(i, curr, nxt)
      forward.append(seq | (set() if not forward else forward[-1]))
      
    curr = set([(0, 0)])
    for i in range(n-1, -1, -1):
      seq, curr, nxt = calc(i, curr, nxt)
      backward.append(seq | (set() if not backward else backward[-1]))
      
    backward = backward[::-1]
    # print('foward:', forward)
    # print('backward:', backward)
      
    ans = 0
    for i in range(n-1):
      f = forward[i]
      b = backward[i+1]
      
      if not b:
        break
        
      for fv in f:
        for bv in b:
          ans = max(ans, fv^bv)
          # print('xor:', (fv, bv), fv^bv)
    
    return ans
    