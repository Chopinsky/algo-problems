'''
'''


from collections import defaultdict
from typing import List


class Solution:
  '''
  the idea is that for binary values to equal, there must be (3 * bit-1) ones
  in the array, and we can divide these ones into three parts: left, middle,
  and right; to each part, the distance of the ones in the array must equal, 
  i.e. the padding-0s between 1s must be the same; we can ignore all leading
  0s, but the trailing 0s must equal as well (determined from the right parts),
  and the trailing 0s must not be longer than the 1st bit-1 in the next part.
  '''
  def threeEqualParts(self, arr: List[int]) -> List[int]:
    ones = []
    
    # take a note of all position of 1s
    for i, bit in enumerate(arr):
      if bit == 1:
        ones.append(i)
        
    if len(ones) == 0:
      return [0, 2]
    
    if len(ones) % 3 != 0:
      return [-1, -1]
    
    # divide positions of 1s into 3 parts
    seg_size = len(ones) // 3
    l, m, r = ones[:seg_size], ones[seg_size:2*seg_size], ones[2*seg_size:]
    # print(len(l), len(m), len(r))
    
    if len(l) > 1:
      # each 1s in their matching index position shall have equal 0-paddings
      for i in range(1, seg_size):
        dist = l[i] - l[i-1]
        if dist != m[i]-m[i-1] or dist != r[i]-r[i-1]:
          return [-1, -1]
    
    trailing_zeros = len(arr)-1-r[-1]
    lb, mb = l[-1]+trailing_zeros, m[-1]+trailing_zeros
    
    # the trailing zero paddings must not overflow to the next segment, i.e.
    # we don't have enough zero paddings for the left or middle parts
    return [lb, mb] if (lb < m[0] and mb < r[0]) else [-1, -1]
      
    
  def threeEqualParts1(self, arr: List[int]) -> List[int]:
    p = 0
    while p < len(arr) and arr[p] == 0:
      p += 1
      
    arr = arr[p:]
    if not arr:
      return [0, p-1]
    
    ln = len(arr)
    if ln < 3:
      return [-1, -1]
    
    l, r, top = 0, 0, 1
    ld, rd = {}, defaultdict(list)
    # md = {}
    
    def get_val(a: List[int]) -> int:
      if not a:
        return -1
      
      base = a[0]
      
      for n in range(1, len(a)):
        base <<= 1
        base |= a[n]
        
      return base
    
    for i in range(ln-2):
      l <<= 1
      l |= arr[i]
      
      if arr[ln-i-1] == 1:
        r |= top
        
      top <<= 1
      ld[l] = i
      rd[r].append(ln-i-1)
      
    # print(ld, rd)
    
    for val, i in ld.items():
      if val not in rd:
        continue
      
      m = -1
      last = -1
      
      for j in rd[val]:
        if i+1 >= j:
          break
        
        if m < 0:
          m = get_val(arr[i+1:j])
        else:
          k = last
          while k > j:
            m >>= 1
            k -= 1
          
        # print("left:", l, i, rd[l], m)
        last = j
        if m == val:
          return [i+p, j+p]
    
    return [-1, -1]
    