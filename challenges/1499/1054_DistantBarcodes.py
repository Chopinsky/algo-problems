'''
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]

Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''


from typing import List
from collections import Counter


class Solution:
  def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    n = len(barcodes)
    ans = [0] * n
    c = Counter(barcodes)
    s = sorted(c, key=lambda x: c[x])
    curr = s.pop()
    # print(c, s)
    
    for i in range(0, n, 2):
      if c[curr] == 0:
        curr = s.pop()
      
      ans[i] = curr
      c[curr] -= 1
    
    for i in range(1, n, 2):
      if c[curr] == 0:
        curr = s.pop()
        
      ans[i] = curr
      c[curr] -= 1
      
    return ans
    