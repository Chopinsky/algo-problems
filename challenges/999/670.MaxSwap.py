'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 10^8
'''


from typing import Counter


class Solution:
  def maximumSwap(self, num: int) -> int:
    d = list(str(num))
    n = len(d)
    c = Counter(d)
    top = sorted(c)
    
    idx = 0
    while idx < n and d[idx] == top[-1]:
      val = d[idx]
      c[val] -= 1
      
      if not c[val]:
        c.pop(val, None)
        top.pop()
        
      idx += 1

    if idx+1 < n:
      bigger_num_idx = idx
      jdx = idx+1
      
      while jdx < n:
        if d[jdx] >= d[bigger_num_idx]:
          bigger_num_idx = jdx
          
        jdx += 1
        
      d[idx], d[bigger_num_idx] = d[bigger_num_idx], d[idx]
    
    return int(''.join(d))
  